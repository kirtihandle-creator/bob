from datetime import date, timedelta
WORKFLOW_ID = 'python_app_design'
NAME = 'Python application: Design'
CATEGORY = 'python_app'
PHASE = 'design'
TASKS = (
    {
        "title": 'Python application: review requirements',
        "notes": 'Review requirements for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Python application: sketch the structure',
        "notes": 'Sketch the structure for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Python application: describe the main flow',
        "notes": 'Describe the main flow for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Python application: define inputs',
        "notes": 'Define inputs for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Python application: define outputs',
        "notes": 'Define outputs for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Python application: choose naming conventions',
        "notes": 'Choose naming conventions for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Python application: design error handling',
        "notes": 'Design error handling for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Python application: check accessibility needs',
        "notes": 'Check accessibility needs for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Python application: create an example',
        "notes": 'Create an example for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Python application: compare design options',
        "notes": 'Compare design options for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Python application: review design decisions',
        "notes": 'Review design decisions for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Python application: finalize the design notes',
        "notes": 'Finalize the design notes for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
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
