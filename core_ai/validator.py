def validate_task(task: str) -> bool:
    """
    Basic safety and sanity validation for planned tasks.
    """
    blocked_keywords = [
        "illegal",
        "hack",
        "exploit",
        "malware",
        "unauthorized"
    ]

    task_lower = task.lower()
    return not any(word in task_lower for word in blocked_keywords)
