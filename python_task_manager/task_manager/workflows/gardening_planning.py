from datetime import date, timedelta
WORKFLOW_ID = 'gardening_planning'
NAME = 'Gardening project: Planning'
CATEGORY = 'gardening'
PHASE = 'planning'
TASKS = (
    {
        "title": 'Gardening project: define the outcome',
        "notes": 'Define the outcome for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Gardening project: set success criteria',
        "notes": 'Set success criteria for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Gardening project: break down the work',
        "notes": 'Break down the work for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Gardening project: estimate task effort',
        "notes": 'Estimate task effort for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Gardening project: identify dependencies',
        "notes": 'Identify dependencies for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Gardening project: assign responsibilities',
        "notes": 'Assign responsibilities for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Gardening project: set milestones',
        "notes": 'Set milestones for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Gardening project: reserve review time',
        "notes": 'Reserve review time for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Gardening project: record delivery risks',
        "notes": 'Record delivery risks for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Gardening project: choose progress measures',
        "notes": 'Choose progress measures for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Gardening project: review the schedule',
        "notes": 'Review the schedule for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Gardening project: approve the working plan',
        "notes": 'Approve the working plan for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
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
