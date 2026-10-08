from datetime import date, timedelta
WORKFLOW_ID = 'community_maintenance'
NAME = 'Community project: Maintenance'
CATEGORY = 'community'
PHASE = 'maintenance'
TASKS = (
    {
        "title": 'Community project: review recent feedback',
        "notes": 'Review recent feedback for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Community project: inventory open issues',
        "notes": 'Inventory open issues for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Community project: check supporting resources',
        "notes": 'Check supporting resources for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Community project: identify outdated material',
        "notes": 'Identify outdated material for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Community project: prioritize maintenance work',
        "notes": 'Prioritize maintenance work for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Community project: back up the current state',
        "notes": 'Back up the current state for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Community project: apply a focused improvement',
        "notes": 'Apply a focused improvement for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Community project: check existing behavior',
        "notes": 'Check existing behavior for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Community project: update supporting notes',
        "notes": 'Update supporting notes for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Community project: verify recovery steps',
        "notes": 'Verify recovery steps for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Community project: record maintenance changes',
        "notes": 'Record maintenance changes for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Community project: schedule the next review',
        "notes": 'Schedule the next review for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
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
