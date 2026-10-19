import pytest

from engine.engine import WorkflowEngine
from engine.errors import UnknownWorkflowError
from engine.workflows import dual_review_config


@pytest.fixture
def engine():
    return WorkflowEngine()


@pytest.fixture
def wf_id(engine):
    return engine.register_workflow(dual_review_config)


def new_dp(engine, wf_id, start=True):
    dp = engine.create_datapoint(wf_id)
    if start:
        engine.start(dp)
    return dp


def review(engine, dp, a, b):
    engine.complete_task(dp, "submission", "submit")
    engine.complete_task(dp, "review_a", a)
    engine.complete_task(dp, "review_b", b)


@pytest.fixture
def populated(engine, wf_id):
    """accepted (r1), accepted via reauthor (r2), rejected via adjudication (r1),
    one waiting on review_b, one pending."""
    review(engine, new_dp(engine, wf_id), "approve", "approve")

    dp = new_dp(engine, wf_id)
    review(engine, dp, "reject", "reject")
    review(engine, dp, "approve", "approve")

    dp = new_dp(engine, wf_id)
    review(engine, dp, "approve", "reject")
    engine.complete_task(dp, "adjudication", "reject")

    dp = new_dp(engine, wf_id)
    engine.complete_task(dp, "submission", "submit")
    engine.complete_task(dp, "review_a", "approve")

    new_dp(engine, wf_id, start=False)
    return wf_id


def test_empty_workflow(engine, wf_id):
    a = engine.analytics
    assert a.outcomes(wf_id) == {}
    assert a.average_rounds(wf_id) == 0.0
    assert a.completions_by_task(wf_id) == {}
    assert a.current_states(wf_id) == {}


def test_outcomes(engine, populated):
    assert engine.analytics.outcomes(populated) == {"accepted": 2, "rejected": 1}


def test_average_rounds(engine, populated):
    # rounds: 1, 2, 1, 1, 1
    assert engine.analytics.average_rounds(populated) == pytest.approx(6 / 5)


def test_completions_by_task(engine, populated):
    assert engine.analytics.completions_by_task(populated) == {
        "submission": 5,
        "review_a": 5,
        "review_b": 4,
        "adjudication": 1,
    }


def test_current_states(engine, populated):
    assert engine.analytics.current_states(populated) == {
        "accepted": 2,
        "rejected": 1,
        "review_b": 1,
        "pending": 1,
    }


def test_parallel_reviews_count_once_per_active_task(engine, wf_id):
    dp = new_dp(engine, wf_id)
    engine.complete_task(dp, "submission", "submit")
    assert engine.analytics.current_states(wf_id) == {"review_a": 1, "review_b": 1}


def test_workflows_are_isolated(engine, wf_id):
    other = engine.register_workflow(dual_review_config)
    review(engine, new_dp(engine, wf_id), "approve", "approve")
    assert engine.analytics.outcomes(other) == {}
    assert engine.analytics.completions_by_task(other) == {}


@pytest.mark.parametrize(
    "method", ["outcomes", "average_rounds", "completions_by_task", "current_states"]
)
def test_unknown_workflow(engine, method):
    with pytest.raises(UnknownWorkflowError):
        getattr(engine.analytics, method)("nope")
