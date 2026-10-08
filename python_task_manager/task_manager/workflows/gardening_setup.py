from datetime import date, timedelta
WORKFLOW_ID = 'gardening_setup'
NAME = 'Gardening project: Setup'
CATEGORY = 'gardening'
PHASE = 'setup'
TASKS = (
    {
        "title": 'Gardening project: inventory required tools',
        "notes": 'Inventory required tools for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Gardening project: create the workspace',
        "notes": 'Create the workspace for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Gardening project: define the folder structure',
        "notes": 'Define the folder structure for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Gardening project: configure local settings',
        "notes": 'Configure local settings for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Gardening project: prepare sample inputs',
        "notes": 'Prepare sample inputs for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Gardening project: create a work log',
        "notes": 'Create a work log for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Gardening project: set up version tracking',
        "notes": 'Set up version tracking for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Gardening project: document setup steps',
        "notes": 'Document setup steps for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Gardening project: check required access',
        "notes": 'Check required access for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Gardening project: run a small trial',
        "notes": 'Run a small trial for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Gardening project: resolve setup issues',
        "notes": 'Resolve setup issues for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Gardening project: confirm readiness',
        "notes": 'Confirm readiness for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
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
