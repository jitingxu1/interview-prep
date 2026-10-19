"""
Workflow configurations.

Must export: dual_review_config

Config format:
  start            -- tasks activated when a datapoint starts
  authoring_task   -- re-entering this task starts a new round
  terminal_states  -- final states a datapoint can end in
  tasks            -- {task: {result: target}}
  joins            -- {join: {"wait_for": [tasks], "rules": {rule: target}}}

A target is a task name, a terminal state, "join:<name>", or a list of
task names (activated in parallel). Join rules are checked in order:
"all:<result>", "any:<result>", and a required "default".
"""

dual_review_config = {
    "name": "dual_review",
    "start": ["submission"],
    "authoring_task": "submission",
    "terminal_states": ["accepted", "rejected"],
    "tasks": {
        "submission": {"submit": ["review_a", "review_b"]},
        "review_a": {"approve": "join:reviews", "reject": "join:reviews"},
        "review_b": {"approve": "join:reviews", "reject": "join:reviews"},
        "adjudication": {"approve": "accepted", "reject": "rejected", "revise": "submission"},
    },
    "joins": {
        "reviews": {
            "wait_for": ["review_a", "review_b"],
            "rules": {
                "all:approve": "accepted",
                "all:reject": "submission",
                "default": "adjudication",
            },
        },
    },
}
