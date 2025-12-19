
"""
executor.py
Responsible for executing validated tasks produced by the planner.
"""

from typing import List, Dict
from core_ai.validator import validate_task


class TaskExecutionError(Exception):
    """Raised when a task cannot be executed safely."""
    pass


def execute_tasks(tasks: List[str]) -> Dict[str, str]:
    """
    Execute a list of validated tasks sequentially.

    Args:
        tasks (List[str]): List of task descriptions.

    Returns:
        Dict[str, str]: Execution results for each task.
    """

    results = {}

    for index, task in enumerate(tasks, start=1):
        # Safety check
        if not validate_task(task):
            raise TaskExecutionError(
                f"Task '{task}' failed validation and was blocked."
            )

        # Simulated execution (placeholder for real execution logic)
        result = _simulate_execution(task)

        results[f"task_{index}"] = result

    return results


def _simulate_execution(task: str) -> str:
    """
    Simulate task execution.
    Replace this with real execution logic later
    (API calls, simulations, robotics, workflows, etc.).
    """
    return f"Executed successfully: {task}"
