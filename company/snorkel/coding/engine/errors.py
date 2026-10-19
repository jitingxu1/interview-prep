"""
Errors raised by the workflow engine.

All errors subclass ValueError so callers can catch them generically.
"""


class WorkflowError(ValueError):
    """Base class for all workflow engine errors."""


class InvalidConfigError(WorkflowError):
    """The workflow config is malformed."""


class UnknownWorkflowError(WorkflowError):
    """No workflow is registered under the given id."""


class InvalidStateError(WorkflowError):
    """The datapoint is not in a state that allows this operation."""


class InvalidTaskError(WorkflowError):
    """The task is not currently active on the datapoint."""


class InvalidResultError(WorkflowError):
    """The result is not valid for the task."""
