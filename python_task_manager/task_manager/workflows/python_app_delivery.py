from datetime import date, timedelta
WORKFLOW_ID = 'python_app_delivery'
NAME = 'Python application: Delivery'
CATEGORY = 'python_app'
PHASE = 'delivery'
TASKS = (
    {
        "title": 'Python application: confirm delivery scope',
        "notes": 'Confirm delivery scope for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Python application: check outstanding issues',
        "notes": 'Check outstanding issues for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Python application: prepare final materials',
        "notes": 'Prepare final materials for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Python application: write usage instructions',
        "notes": 'Write usage instructions for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Python application: document known limitations',
        "notes": 'Document known limitations for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Python application: prepare a demonstration',
        "notes": 'Prepare a demonstration for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Python application: check destination requirements',
        "notes": 'Check destination requirements for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Python application: create a backup copy',
        "notes": 'Create a backup copy for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Python application: verify the delivery package',
        "notes": 'Verify the delivery package for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Python application: complete the handoff',
        "notes": 'Complete the handoff for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Python application: confirm recipient access',
        "notes": 'Confirm recipient access for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Python application: record the delivered version',
        "notes": 'Record the delivered version for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 5,
    },
)
def build_tasks(start_date=None):
    base = date.today() if start_date is None else date.fromisoformat(start_date)
    return [
        {
            "title": item["title"],
            "notes": item["notes"],
            "priority": item["priority"],
            "due_date": (base + timedelta(days=item["day_offset"])).isoformat(),
        }
        for item in TASKS
    ]
def summary():
    return {
        "id": WORKFLOW_ID,
        "name": NAME,
        "category": CATEGORY,
        "phase": PHASE,
        "task_count": len(TASKS),
        "duration_days": max(item["day_offset"] for item in TASKS) + 1,
        "high_priority_tasks": sum(item["priority"] == "High" for item in TASKS),
    }
