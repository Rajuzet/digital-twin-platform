
"""
main.py
Entry point for the Digital Twin AI system
"""

from core_ai.planner import plan_goal
from core_ai.executor import execute_tasks


def main():
    # Example high-level goal
    goal = "Build a digital twin system for satellite mission planning"

    print("🎯 Goal:")
    print(goal)
    print("\n🧠 Planning...\n")

    # Step 1: Plan the goal
    plan = plan_goal(goal)
    tasks = plan.get("tasks", [])

    if not tasks:
        print("❌ No tasks generated.")
        return

    print("📋 Planned Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

    print("\n⚙️ Executing tasks...\n")

    # Step 2: Execute tasks
    results = execute_tasks(tasks)

    print("✅ Execution Results:")
    for task_id, result in results.items():
        print(f"{task_id}: {result}")


if __name__ == "__main__":
    main()
  
