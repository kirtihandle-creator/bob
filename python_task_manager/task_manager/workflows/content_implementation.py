from datetime import date, timedelta
WORKFLOW_ID = 'content_implementation'
NAME = 'Content project: Implementation'
CATEGORY = 'content'
PHASE = 'implementation'
TASKS = (
    {
        "title": 'Content project: select the first milestone',
        "notes": 'Select the first milestone for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Content project: prepare the input material',
        "notes": 'Prepare the input material for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Content project: build the core deliverable',
        "notes": 'Build the core deliverable for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Content project: handle common variations',
        "notes": 'Handle common variations for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Content project: handle missing inputs',
        "notes": 'Handle missing inputs for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Content project: add useful feedback',
        "notes": 'Add useful feedback for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Content project: connect the main components',
        "notes": 'Connect the main components for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Content project: review naming and structure',
        "notes": 'Review naming and structure for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Content project: remove duplicated work',
        "notes": 'Remove duplicated work for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Content project: document key decisions',
        "notes": 'Document key decisions for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Content project: run the main workflow',
        "notes": 'Run the main workflow for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Content project: record remaining gaps',
        "notes": 'Record remaining gaps for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
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
