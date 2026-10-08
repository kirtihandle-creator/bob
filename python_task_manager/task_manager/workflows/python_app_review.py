from datetime import date, timedelta
WORKFLOW_ID = 'python_app_review'
NAME = 'Python application: Review'
CATEGORY = 'python_app'
PHASE = 'review'
TASKS = (
    {
        "title": 'Python application: collect the current deliverables',
        "notes": 'Collect the current deliverables for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Python application: review the original goals',
        "notes": 'Review the original goals for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Python application: check completeness',
        "notes": 'Check completeness for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Python application: check internal consistency',
        "notes": 'Check internal consistency for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Python application: review supporting evidence',
        "notes": 'Review supporting evidence for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Python application: review usability',
        "notes": 'Review usability for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Python application: identify confusing sections',
        "notes": 'Identify confusing sections for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Python application: collect reviewer feedback',
        "notes": 'Collect reviewer feedback for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Python application: prioritize requested changes',
        "notes": 'Prioritize requested changes for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Python application: apply agreed changes',
        "notes": 'Apply agreed changes for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Python application: verify the revised work',
        "notes": 'Verify the revised work for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Python application: record review decisions',
        "notes": 'Record review decisions for the python application. Focus on application behavior and maintainable Python code. Record the outcome and any follow-up needed in your task notes.',
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
