"""
Models for the annotation workflow engine.

Must export: DatapointStatus
"""

from dataclasses import dataclass
from enum import Enum


class DatapointStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


@dataclass(frozen=True)
class HistoryEntry:
    """One completed task: which task, the result given, and the round it happened in."""

    task: str
    result: str
    round: int


class Datapoint:
    """A single item moving through a workflow. The engine updates it in place."""

    def __init__(self, workflow_id: str):
        self.workflow_id = workflow_id
        self._status = DatapointStatus.PENDING
        self._active_tasks: set[str] = set()
        self._round = 1
        self._final_state: str | None = None
        self._history: list[HistoryEntry] = []
        # join name -> {task name -> result}, collected until the join fires
        self._join_results: dict[str, dict[str, str]] = {}

    @property
    def status(self) -> DatapointStatus:
        """Current status of the datapoint."""
        return self._status

    @property
    def active_tasks(self) -> set[str]:
        """Names of the currently active tasks."""
        return set(self._active_tasks)

    @property
    def current_round(self) -> int:
        """Current round of the datapoint."""
        return self._round

    @property
    def final_state(self) -> str | None:
        """Final state once completed, otherwise None."""
        return self._final_state

    @property
    def history(self) -> list:
        """Ordered record of completed tasks."""
        return list(self._history)

    def __repr__(self) -> str:
        return (
            f"Datapoint(workflow_id={self.workflow_id!r}, status={self._status.value}, "
            f"active={sorted(self._active_tasks)}, round={self._round}, "
            f"final_state={self._final_state!r})"
        )
