from datetime import date, timedelta
WORKFLOW_ID = 'python_app_retrospective'
NAME = 'Python application: Retrospective'
CATEGORY = 'python_app'
PHASE = 'retrospective'
TASKS = (
    {
        "title": 'Python application: collect outcome measures',
        "notes": 'Collect outcome measures for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Python application: compare results with goals',
        "notes": 'Compare results with goals for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Python application: review the project timeline',
        "notes": 'Review the project timeline for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Python application: identify successful practices',
        "notes": 'Identify successful practices for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Python application: identify recurring obstacles',
        "notes": 'Identify recurring obstacles for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Python application: review effort estimates',
        "notes": 'Review effort estimates for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Python application: collect participant feedback',
        "notes": 'Collect participant feedback for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Python application: document surprising findings',
        "notes": 'Document surprising findings for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Python application: choose process improvements',
        "notes": 'Choose process improvements for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Python application: assign follow-up actions',
        "notes": 'Assign follow-up actions for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Python application: archive useful materials',
        "notes": 'Archive useful materials for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Python application: write the retrospective summary',
        "notes": 'Write the retrospective summary for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
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
