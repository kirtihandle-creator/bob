from datetime import date, timedelta
WORKFLOW_ID = 'python_app_planning'
NAME = 'Python application: Planning'
CATEGORY = 'python_app'
PHASE = 'planning'
TASKS = (
    {
        "title": 'Python application: define the outcome',
        "notes": 'Define the outcome for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Python application: set success criteria',
        "notes": 'Set success criteria for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Python application: break down the work',
        "notes": 'Break down the work for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Python application: estimate task effort',
        "notes": 'Estimate task effort for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Python application: identify dependencies',
        "notes": 'Identify dependencies for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Python application: assign responsibilities',
        "notes": 'Assign responsibilities for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Python application: set milestones',
        "notes": 'Set milestones for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Python application: reserve review time',
        "notes": 'Reserve review time for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Python application: record delivery risks',
        "notes": 'Record delivery risks for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Python application: choose progress measures',
        "notes": 'Choose progress measures for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Python application: review the schedule',
        "notes": 'Review the schedule for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Python application: approve the working plan',
        "notes": 'Approve the working plan for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
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
