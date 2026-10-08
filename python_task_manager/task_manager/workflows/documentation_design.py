from datetime import date, timedelta
WORKFLOW_ID = 'documentation_design'
NAME = 'Documentation: Design'
CATEGORY = 'documentation'
PHASE = 'design'
TASKS = (
    {
        "title": 'Documentation: review requirements',
        "notes": 'Review requirements for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Documentation: sketch the structure',
        "notes": 'Sketch the structure for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Documentation: describe the main flow',
        "notes": 'Describe the main flow for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Documentation: define inputs',
        "notes": 'Define inputs for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Documentation: define outputs',
        "notes": 'Define outputs for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Documentation: choose naming conventions',
        "notes": 'Choose naming conventions for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Documentation: design error handling',
        "notes": 'Design error handling for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Documentation: check accessibility needs',
        "notes": 'Check accessibility needs for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Documentation: create an example',
        "notes": 'Create an example for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Documentation: compare design options',
        "notes": 'Compare design options for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Documentation: review design decisions',
        "notes": 'Review design decisions for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Documentation: finalize the design notes',
        "notes": 'Finalize the design notes for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
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
