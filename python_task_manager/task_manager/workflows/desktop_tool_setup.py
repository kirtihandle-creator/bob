from datetime import date, timedelta
WORKFLOW_ID = 'desktop_tool_setup'
NAME = 'Desktop tool: Setup'
CATEGORY = 'desktop_tool'
PHASE = 'setup'
TASKS = (
    {
        "title": 'Desktop tool: inventory required tools',
        "notes": 'Inventory required tools for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Desktop tool: create the workspace',
        "notes": 'Create the workspace for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Desktop tool: define the folder structure',
        "notes": 'Define the folder structure for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Desktop tool: configure local settings',
        "notes": 'Configure local settings for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Desktop tool: prepare sample inputs',
        "notes": 'Prepare sample inputs for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Desktop tool: create a work log',
        "notes": 'Create a work log for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Desktop tool: set up version tracking',
        "notes": 'Set up version tracking for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Desktop tool: document setup steps',
        "notes": 'Document setup steps for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Desktop tool: check required access',
        "notes": 'Check required access for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Desktop tool: run a small trial',
        "notes": 'Run a small trial for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Desktop tool: resolve setup issues',
        "notes": 'Resolve setup issues for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Desktop tool: confirm readiness',
        "notes": 'Confirm readiness for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
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
