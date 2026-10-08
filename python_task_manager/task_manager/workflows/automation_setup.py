from datetime import date, timedelta
WORKFLOW_ID = 'automation_setup'
NAME = 'Automation: Setup'
CATEGORY = 'automation'
PHASE = 'setup'
TASKS = (
    {
        "title": 'Automation: inventory required tools',
        "notes": 'Inventory required tools for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Automation: create the workspace',
        "notes": 'Create the workspace for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Automation: define the folder structure',
        "notes": 'Define the folder structure for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Automation: configure local settings',
        "notes": 'Configure local settings for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Automation: prepare sample inputs',
        "notes": 'Prepare sample inputs for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Automation: create a work log',
        "notes": 'Create a work log for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Automation: set up version tracking',
        "notes": 'Set up version tracking for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Automation: document setup steps',
        "notes": 'Document setup steps for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Automation: check required access',
        "notes": 'Check required access for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Automation: run a small trial',
        "notes": 'Run a small trial for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Automation: resolve setup issues',
        "notes": 'Resolve setup issues for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Automation: confirm readiness',
        "notes": 'Confirm readiness for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
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
