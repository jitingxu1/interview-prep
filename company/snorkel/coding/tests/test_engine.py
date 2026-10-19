import copy

import pytest

from engine.engine import WorkflowEngine
from engine.errors import (
    InvalidConfigError,
    InvalidResultError,
    InvalidStateError,
    InvalidTaskError,
    UnknownWorkflowError,
)
from engine.models import DatapointStatus, HistoryEntry
from engine.workflows import dual_review_config

SINGLE_REVIEW = {
    "start": ["submission"],
    "authoring_task": "submission",
    "terminal_states": ["accepted"],
    "tasks": {
        "submission": {"submit": "review"},
        "review": {"approve": "accepted", "reject": "submission"},
    },
}


@pytest.fixture
def engine():
    return WorkflowEngine()


@pytest.fixture
def dp(engine):
    wf_id = engine.register_workflow(dual_review_config)
    dp = engine.create_datapoint(wf_id)
    engine.start(dp)
    return dp


def submit_and_review(engine, dp, a, b):
    engine.complete_task(dp, "submission", "submit")
    engine.complete_task(dp, "review_a", a)
    engine.complete_task(dp, "review_b", b)


def test_new_datapoint_is_pending(engine):
    dp = engine.create_datapoint(engine.register_workflow(dual_review_config))
    assert dp.status is DatapointStatus.PENDING
    assert dp.active_tasks == set()
    assert dp.current_round == 1
    assert dp.final_state is None
    assert dp.history == []


def test_start_activates_start_tasks(dp):
    assert dp.status is DatapointStatus.IN_PROGRESS
    assert dp.active_tasks == {"submission"}


def test_submit_activates_both_reviews_in_parallel(engine, dp):
    engine.complete_task(dp, "submission", "submit")
    assert dp.active_tasks == {"review_a", "review_b"}
    engine.complete_task(dp, "review_b", "approve")
    assert dp.active_tasks == {"review_a"}
    assert dp.status is DatapointStatus.IN_PROGRESS


def test_both_approve_accepts(engine, dp):
    submit_and_review(engine, dp, "approve", "approve")
    assert dp.status is DatapointStatus.COMPLETED
    assert dp.final_state == "accepted"
    assert dp.active_tasks == set()
    assert dp.current_round == 1
    assert dp.history == [
        HistoryEntry("submission", "submit", 1),
        HistoryEntry("review_a", "approve", 1),
        HistoryEntry("review_b", "approve", 1),
    ]


def test_both_reject_reauthors_and_increments_round(engine, dp):
    submit_and_review(engine, dp, "reject", "reject")
    assert dp.active_tasks == {"submission"}
    assert dp.current_round == 2
    submit_and_review(engine, dp, "approve", "approve")
    assert dp.final_state == "accepted"
    assert dp.current_round == 2
    assert [h.round for h in dp.history] == [1, 1, 1, 2, 2, 2]


@pytest.mark.parametrize("a, b", [("approve", "reject"), ("reject", "approve")])
def test_disagreement_goes_to_adjudication(engine, dp, a, b):
    submit_and_review(engine, dp, a, b)
    assert dp.active_tasks == {"adjudication"}
    assert dp.current_round == 1


@pytest.mark.parametrize("result, final", [("approve", "accepted"), ("reject", "rejected")])
def test_adjudication_terminal_outcomes(engine, dp, result, final):
    submit_and_review(engine, dp, "approve", "reject")
    engine.complete_task(dp, "adjudication", result)
    assert dp.status is DatapointStatus.COMPLETED
    assert dp.final_state == final


def test_full_walkthrough_with_revise(engine, dp):
    submit_and_review(engine, dp, "approve", "reject")
    engine.complete_task(dp, "adjudication", "revise")
    assert dp.active_tasks == {"submission"}
    assert dp.current_round == 2
    submit_and_review(engine, dp, "approve", "approve")
    assert dp.final_state == "accepted"
    assert len(dp.history) == 7


def test_join_results_do_not_leak_between_rounds(engine, dp):
    submit_and_review(engine, dp, "reject", "reject")
    engine.complete_task(dp, "submission", "submit")
    engine.complete_task(dp, "review_a", "approve")
    # review_b from round 1 must not count; the join still waits for it.
    assert dp.active_tasks == {"review_b"}


def test_single_review_workflow(engine):
    dp = engine.create_datapoint(engine.register_workflow(SINGLE_REVIEW))
    engine.start(dp)
    engine.complete_task(dp, "submission", "submit")
    engine.complete_task(dp, "review", "reject")
    engine.complete_task(dp, "submission", "submit")
    engine.complete_task(dp, "review", "approve")
    assert dp.final_state == "accepted"
    assert dp.current_round == 2


def test_properties_return_copies(engine, dp):
    dp.active_tasks.add("hacked")
    dp.history.append("hacked")
    assert dp.active_tasks == {"submission"}
    assert dp.history == []


def test_registered_config_is_isolated_from_caller(engine):
    config = copy.deepcopy(SINGLE_REVIEW)
    wf_id = engine.register_workflow(config)
    config["tasks"]["review"]["approve"] = "submission"
    dp = engine.create_datapoint(wf_id)
    engine.start(dp)
    engine.complete_task(dp, "submission", "submit")
    engine.complete_task(dp, "review", "approve")
    assert dp.final_state == "accepted"


def test_each_registration_gets_new_id(engine):
    assert engine.register_workflow(dual_review_config) != engine.register_workflow(dual_review_config)


# --- errors -----------------------------------------------------------------


def test_unknown_workflow(engine):
    with pytest.raises(UnknownWorkflowError):
        engine.create_datapoint("nope")


def test_start_twice(engine, dp):
    with pytest.raises(InvalidStateError):
        engine.start(dp)


def test_complete_before_start(engine):
    dp = engine.create_datapoint(engine.register_workflow(dual_review_config))
    with pytest.raises(InvalidStateError):
        engine.complete_task(dp, "submission", "submit")


def test_complete_inactive_task(engine, dp):
    with pytest.raises(InvalidTaskError):
        engine.complete_task(dp, "review_a", "approve")


def test_complete_unknown_task(engine, dp):
    with pytest.raises(InvalidTaskError):
        engine.complete_task(dp, "nope", "submit")


def test_invalid_result(engine, dp):
    with pytest.raises(InvalidResultError):
        engine.complete_task(dp, "submission", "maybe")
    assert dp.history == []
    assert dp.active_tasks == {"submission"}


def test_same_review_cannot_complete_twice(engine, dp):
    engine.complete_task(dp, "submission", "submit")
    engine.complete_task(dp, "review_a", "approve")
    with pytest.raises(InvalidTaskError):
        engine.complete_task(dp, "review_a", "reject")


def test_actions_after_completion(engine, dp):
    submit_and_review(engine, dp, "approve", "approve")
    with pytest.raises(InvalidStateError):
        engine.complete_task(dp, "submission", "submit")
    with pytest.raises(InvalidStateError):
        engine.start(dp)


def test_errors_are_value_errors(engine):
    with pytest.raises(ValueError):
        engine.create_datapoint("nope")


def _with(**changes):
    config = copy.deepcopy(dual_review_config)
    config.update(changes)
    return config


@pytest.mark.parametrize(
    "config",
    [
        None,
        {},
        _with(tasks={}),
        _with(start=[]),
        _with(start=["nope"]),
        _with(authoring_task="nope"),
        _with(terminal_states=[]),
        _with(terminal_states=["accepted", "submission"]),
        _with(tasks={**dual_review_config["tasks"], "submission": {}}),
        _with(tasks={**dual_review_config["tasks"], "submission": {"submit": "nowhere"}}),
        _with(tasks={**dual_review_config["tasks"], "submission": {"submit": ["review_a", "accepted"]}}),
        _with(tasks={**dual_review_config["tasks"], "review_a": {"approve": "accepted", "reject": "join:reviews"}}),
        _with(tasks={**dual_review_config["tasks"], "submission": {"submit": "join:missing"}}),
        _with(joins={"reviews": {"wait_for": ["review_a", "review_b"], "rules": {"all:approve": "accepted"}}}),
        _with(joins={"reviews": {"wait_for": ["review_a", "review_b"], "rules": {"most:approve": "accepted", "default": "adjudication"}}}),
        _with(joins={"reviews": {"wait_for": ["review_a"], "rules": {"default": "adjudication"}}}),
        _with(joins={"reviews": {"wait_for": ["review_a", "review_b"], "rules": {"default": "join:reviews"}}}),
    ],
)
def test_invalid_configs(engine, config):
    with pytest.raises(InvalidConfigError):
        engine.register_workflow(config)
