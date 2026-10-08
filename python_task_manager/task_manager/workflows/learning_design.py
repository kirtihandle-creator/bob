from datetime import date, timedelta
WORKFLOW_ID = 'learning_design'
NAME = 'Learning program: Design'
CATEGORY = 'learning'
PHASE = 'design'
TASKS = (
    {
        "title": 'Learning program: review requirements',
        "notes": 'Review requirements for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Learning program: sketch the structure',
        "notes": 'Sketch the structure for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Learning program: describe the main flow',
        "notes": 'Describe the main flow for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Learning program: define inputs',
        "notes": 'Define inputs for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Learning program: define outputs',
        "notes": 'Define outputs for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Learning program: choose naming conventions',
        "notes": 'Choose naming conventions for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Learning program: design error handling',
        "notes": 'Design error handling for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Learning program: check accessibility needs',
        "notes": 'Check accessibility needs for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Learning program: create an example',
        "notes": 'Create an example for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Learning program: compare design options',
        "notes": 'Compare design options for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Learning program: review design decisions',
        "notes": 'Review design decisions for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Learning program: finalize the design notes',
        "notes": 'Finalize the design notes for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
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
