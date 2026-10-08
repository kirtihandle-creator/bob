from datetime import date, timedelta
WORKFLOW_ID = 'gardening_discovery'
NAME = 'Gardening project: Discovery'
CATEGORY = 'gardening'
PHASE = 'discovery'
TASKS = (
    {
        "title": 'Gardening project: define the problem',
        "notes": 'Define the problem for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Gardening project: identify the audience',
        "notes": 'Identify the audience for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Gardening project: collect existing examples',
        "notes": 'Collect existing examples for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Gardening project: record user needs',
        "notes": 'Record user needs for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Gardening project: list constraints',
        "notes": 'List constraints for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Gardening project: review available resources',
        "notes": 'Review available resources for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Gardening project: document assumptions',
        "notes": 'Document assumptions for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Gardening project: identify unknowns',
        "notes": 'Identify unknowns for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Gardening project: compare possible approaches',
        "notes": 'Compare possible approaches for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Gardening project: prioritize opportunities',
        "notes": 'Prioritize opportunities for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Gardening project: summarize findings',
        "notes": 'Summarize findings for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Gardening project: confirm the project brief',
        "notes": 'Confirm the project brief for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
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
