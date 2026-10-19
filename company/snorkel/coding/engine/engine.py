"""
Workflow engine implementation.

Must export: WorkflowEngine
"""

import copy
from collections import Counter

from .errors import (
    InvalidConfigError,
    InvalidResultError,
    InvalidStateError,
    InvalidTaskError,
    UnknownWorkflowError,
)
from .models import Datapoint, DatapointStatus, HistoryEntry

JOIN_PREFIX = "join:"


class WorkflowEngine:
    """Part 1: Core workflow engine."""

    def __init__(self):
        self._workflows: dict[str, dict] = {}
        self._datapoints: dict[str, list[Datapoint]] = {}
        self.analytics = Analytics(self)

    def register_workflow(self, config) -> str:
        """Register a workflow config and return its id. Raises an error if the call is invalid."""
        workflow = _validate_config(copy.deepcopy(config))
        wf_id = f"wf-{len(self._workflows) + 1}"
        self._workflows[wf_id] = workflow
        self._datapoints[wf_id] = []
        return wf_id

    def create_datapoint(self, workflow_id: str) -> Datapoint:
        """Create a new datapoint for the given workflow. Raises an error if the call is invalid."""
        if workflow_id not in self._workflows:
            raise UnknownWorkflowError(f"Unknown workflow id: {workflow_id!r}")
        dp = Datapoint(workflow_id)
        self._datapoints[workflow_id].append(dp)
        return dp

    def start(self, dp: Datapoint) -> None:
        """Start the datapoint on its workflow. Raises an error if the call is invalid."""
        wf = self._workflow_for(dp)
        if dp._status is not DatapointStatus.PENDING:
            raise InvalidStateError(f"Cannot start a datapoint that is {dp._status.value}")
        dp._status = DatapointStatus.IN_PROGRESS
        dp._active_tasks.update(wf["start"])

    def complete_task(self, dp: Datapoint, task_name: str, result: str) -> None:
        """Complete an active task with a result and advance the datapoint. Raises an error if the call is invalid."""
        wf = self._workflow_for(dp)
        if dp._status is not DatapointStatus.IN_PROGRESS:
            raise InvalidStateError(f"Cannot complete a task on a datapoint that is {dp._status.value}")
        if task_name not in dp._active_tasks:
            raise InvalidTaskError(
                f"Task {task_name!r} is not active (active: {sorted(dp._active_tasks)})"
            )
        transitions = wf["tasks"][task_name]
        if result not in transitions:
            raise InvalidResultError(
                f"Invalid result {result!r} for task {task_name!r} (valid: {sorted(transitions)})"
            )

        dp._history.append(HistoryEntry(task_name, result, dp._round))
        dp._active_tasks.discard(task_name)
        self._route(dp, wf, transitions[result], task_name, result)

    def _workflow_for(self, dp: Datapoint) -> dict:
        if not isinstance(dp, Datapoint):
            raise InvalidStateError(f"Expected a Datapoint, got {type(dp).__name__}")
        if dp.workflow_id not in self._workflows:
            raise UnknownWorkflowError(f"Unknown workflow id: {dp.workflow_id!r}")
        return self._workflows[dp.workflow_id]

    def _route(self, dp: Datapoint, wf: dict, targets: list[str], task_name: str, result: str) -> None:
        """Move the datapoint to each target: a terminal state, a join, or a task."""
        for target in targets:
            if target in wf["terminal_states"]:
                dp._status = DatapointStatus.COMPLETED
                dp._final_state = target
                dp._active_tasks.clear()
                dp._join_results.clear()
                return
            if target.startswith(JOIN_PREFIX):
                join_name = target[len(JOIN_PREFIX):]
                join = wf["joins"][join_name]
                collected = dp._join_results.setdefault(join_name, {})
                collected[task_name] = result
                if all(t in collected for t in join["wait_for"]):
                    del dp._join_results[join_name]
                    results = [collected[t] for t in join["wait_for"]]
                    self._route(dp, wf, _resolve_join(join["rules"], results), task_name, result)
                continue
            if target == wf["authoring_task"]:
                dp._round += 1
            dp._active_tasks.add(target)


def _resolve_join(rules: dict[str, list[str]], results: list[str]) -> list[str]:
    """Return the targets of the first rule matching the collected results."""
    for rule, targets in rules.items():
        if rule == "default":
            return targets
        kind, value = rule.split(":", 1)
        if kind == "all" and all(r == value for r in results):
            return targets
        if kind == "any" and any(r == value for r in results):
            return targets
    raise AssertionError("unreachable: validated joins always end with a default rule")


def _validate_config(config) -> dict:
    """Validate a workflow config and return it with every target normalized to a list."""
    if not isinstance(config, dict):
        raise InvalidConfigError("Workflow config must be a dict")
    for key in ("start", "authoring_task", "terminal_states", "tasks"):
        if key not in config:
            raise InvalidConfigError(f"Workflow config is missing {key!r}")

    tasks = config["tasks"]
    if not isinstance(tasks, dict) or not tasks:
        raise InvalidConfigError("'tasks' must be a non-empty dict")

    terminal_states = config["terminal_states"]
    if not isinstance(terminal_states, (list, tuple, set)) or not terminal_states:
        raise InvalidConfigError("'terminal_states' must be a non-empty list")
    terminal_states = set(terminal_states)
    if not all(isinstance(s, str) for s in terminal_states):
        raise InvalidConfigError("Terminal states must be strings")
    overlap = terminal_states & set(tasks)
    if overlap:
        raise InvalidConfigError(f"Names used as both task and terminal state: {sorted(overlap)}")

    joins = config.get("joins", {})
    if not isinstance(joins, dict):
        raise InvalidConfigError("'joins' must be a dict")

    def normalize(target, where: str, allow_join: bool) -> list[str]:
        items = [target] if isinstance(target, str) else target
        if not isinstance(items, (list, tuple)) or not items:
            raise InvalidConfigError(f"{where}: target must be a name or a non-empty list of names")
        for item in items:
            if not isinstance(item, str):
                raise InvalidConfigError(f"{where}: target {item!r} must be a string")
            if item.startswith(JOIN_PREFIX):
                if not allow_join:
                    raise InvalidConfigError(f"{where}: cannot target a join here")
                if item[len(JOIN_PREFIX):] not in joins:
                    raise InvalidConfigError(f"{where}: unknown join {item!r}")
            elif item not in tasks and item not in terminal_states:
                raise InvalidConfigError(f"{where}: unknown target {item!r}")
        if len(items) > 1 and any(item not in tasks for item in items):
            raise InvalidConfigError(f"{where}: a list of targets may only contain tasks")
        return list(items)

    normalized_tasks = {}
    for name, transitions in tasks.items():
        if not isinstance(transitions, dict) or not transitions:
            raise InvalidConfigError(f"Task {name!r} must map at least one result to a target")
        normalized_tasks[name] = {
            result: normalize(target, f"Task {name!r} result {result!r}", allow_join=True)
            for result, target in transitions.items()
        }

    normalized_joins = {}
    for name, join in joins.items():
        if not isinstance(join, dict) or "wait_for" not in join or "rules" not in join:
            raise InvalidConfigError(f"Join {name!r} needs 'wait_for' and 'rules'")
        wait_for = join["wait_for"]
        if not isinstance(wait_for, (list, tuple)) or not wait_for:
            raise InvalidConfigError(f"Join {name!r}: 'wait_for' must be a non-empty list")
        for task in wait_for:
            if task not in tasks:
                raise InvalidConfigError(f"Join {name!r} waits for unknown task {task!r}")
            if any(t != [JOIN_PREFIX + name] for t in normalized_tasks[task].values()):
                raise InvalidConfigError(
                    f"Join {name!r}: every result of task {task!r} must target 'join:{name}'"
                )
        rules = join["rules"]
        if not isinstance(rules, dict) or list(rules)[-1:] != ["default"]:
            raise InvalidConfigError(f"Join {name!r}: rules must be a dict ending with 'default'")
        for rule in rules:
            if rule != "default" and rule.split(":", 1)[0] not in ("all", "any"):
                raise InvalidConfigError(f"Join {name!r}: unknown rule {rule!r}")
        normalized_joins[name] = {
            "wait_for": list(wait_for),
            "rules": {
                rule: normalize(target, f"Join {name!r} rule {rule!r}", allow_join=False)
                for rule, target in rules.items()
            },
        }

    for name, transitions in normalized_tasks.items():
        for targets in transitions.values():
            for target in targets:
                if target.startswith(JOIN_PREFIX) and name not in normalized_joins[target[len(JOIN_PREFIX):]]["wait_for"]:
                    raise InvalidConfigError(f"Task {name!r} targets {target!r} but is not in its 'wait_for'")

    start = config["start"]
    start = [start] if isinstance(start, str) else start
    if not isinstance(start, (list, tuple)) or not start or any(t not in tasks for t in start):
        raise InvalidConfigError("'start' must be a non-empty list of task names")

    if config["authoring_task"] not in tasks:
        raise InvalidConfigError(f"'authoring_task' {config['authoring_task']!r} is not a task")

    return {
        "name": config.get("name"),
        "start": list(start),
        "authoring_task": config["authoring_task"],
        "terminal_states": terminal_states,
        "tasks": normalized_tasks,
        "joins": normalized_joins,
    }


class Analytics:
    """Part 2: Analytics, accessed as `engine.analytics`."""

    def __init__(self, engine: WorkflowEngine):
        self._engine = engine

    def outcomes(self, wf_id: str) -> dict[str, int]:
        """Count of completed datapoints by final state."""
        return dict(Counter(
            dp.final_state for dp in self._datapoints(wf_id)
            if dp.status is DatapointStatus.COMPLETED
        ))

    def average_rounds(self, wf_id: str) -> float:
        """Mean number of rounds across datapoints."""
        dps = self._datapoints(wf_id)
        if not dps:
            return 0.0
        return sum(dp.current_round for dp in dps) / len(dps)

    def completions_by_task(self, wf_id: str) -> dict[str, int]:
        """Total completions per task."""
        return dict(Counter(
            entry.task for dp in self._datapoints(wf_id) for entry in dp.history
        ))

    def current_states(self, wf_id: str) -> dict[str, int]:
        """Number of datapoints at each stage.

        A pending datapoint counts under "pending", a completed one under its final
        state, and an in-progress one under each of its active tasks (so a datapoint
        in parallel review counts once per review task).
        """
        counts: Counter[str] = Counter()
        for dp in self._datapoints(wf_id):
            if dp.status is DatapointStatus.PENDING:
                counts[DatapointStatus.PENDING.value] += 1
            elif dp.status is DatapointStatus.COMPLETED:
                counts[dp.final_state] += 1
            else:
                counts.update(dp.active_tasks)
        return dict(counts)

    def _datapoints(self, wf_id: str) -> list[Datapoint]:
        if wf_id not in self._engine._workflows:
            raise UnknownWorkflowError(f"Unknown workflow id: {wf_id!r}")
        return self._engine._datapoints[wf_id]
