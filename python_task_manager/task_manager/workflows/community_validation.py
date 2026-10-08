from datetime import date, timedelta
WORKFLOW_ID = 'community_validation'
NAME = 'Community project: Validation'
CATEGORY = 'community'
PHASE = 'validation'
TASKS = (
    {
        "title": 'Community project: define acceptance checks',
        "notes": 'Define acceptance checks for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Community project: prepare realistic examples',
        "notes": 'Prepare realistic examples for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Community project: check the normal workflow',
        "notes": 'Check the normal workflow for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Community project: check empty inputs',
        "notes": 'Check empty inputs for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Community project: check invalid inputs',
        "notes": 'Check invalid inputs for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Community project: check boundary conditions',
        "notes": 'Check boundary conditions for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Community project: check repeatability',
        "notes": 'Check repeatability for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Community project: check recovery behavior',
        "notes": 'Check recovery behavior for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Community project: review clarity of feedback',
        "notes": 'Review clarity of feedback for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Community project: record discovered issues',
        "notes": 'Record discovered issues for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Community project: verify corrections',
        "notes": 'Verify corrections for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Community project: summarize validation results',
        "notes": 'Summarize validation results for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
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
