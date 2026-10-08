from datetime import date, timedelta
WORKFLOW_ID = 'learning_implementation'
NAME = 'Learning program: Implementation'
CATEGORY = 'learning'
PHASE = 'implementation'
TASKS = (
    {
        "title": 'Learning program: select the first milestone',
        "notes": 'Select the first milestone for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Learning program: prepare the input material',
        "notes": 'Prepare the input material for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Learning program: build the core deliverable',
        "notes": 'Build the core deliverable for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Learning program: handle common variations',
        "notes": 'Handle common variations for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Learning program: handle missing inputs',
        "notes": 'Handle missing inputs for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Learning program: add useful feedback',
        "notes": 'Add useful feedback for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Learning program: connect the main components',
        "notes": 'Connect the main components for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Learning program: review naming and structure',
        "notes": 'Review naming and structure for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Learning program: remove duplicated work',
        "notes": 'Remove duplicated work for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Learning program: document key decisions',
        "notes": 'Document key decisions for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Learning program: run the main workflow',
        "notes": 'Run the main workflow for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Learning program: record remaining gaps',
        "notes": 'Record remaining gaps for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
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
