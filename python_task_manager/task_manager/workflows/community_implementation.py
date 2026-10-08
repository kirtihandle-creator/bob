from datetime import date, timedelta
WORKFLOW_ID = 'community_implementation'
NAME = 'Community project: Implementation'
CATEGORY = 'community'
PHASE = 'implementation'
TASKS = (
    {
        "title": 'Community project: select the first milestone',
        "notes": 'Select the first milestone for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Community project: prepare the input material',
        "notes": 'Prepare the input material for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Community project: build the core deliverable',
        "notes": 'Build the core deliverable for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Community project: handle common variations',
        "notes": 'Handle common variations for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Community project: handle missing inputs',
        "notes": 'Handle missing inputs for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Community project: add useful feedback',
        "notes": 'Add useful feedback for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Community project: connect the main components',
        "notes": 'Connect the main components for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Community project: review naming and structure',
        "notes": 'Review naming and structure for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Community project: remove duplicated work',
        "notes": 'Remove duplicated work for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Community project: document key decisions',
        "notes": 'Document key decisions for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Community project: run the main workflow',
        "notes": 'Run the main workflow for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Community project: record remaining gaps',
        "notes": 'Record remaining gaps for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
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
