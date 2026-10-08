from datetime import date, timedelta
WORKFLOW_ID = 'automation_maintenance'
NAME = 'Automation: Maintenance'
CATEGORY = 'automation'
PHASE = 'maintenance'
TASKS = (
    {
        "title": 'Automation: review recent feedback',
        "notes": 'Review recent feedback for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Automation: inventory open issues',
        "notes": 'Inventory open issues for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Automation: check supporting resources',
        "notes": 'Check supporting resources for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Automation: identify outdated material',
        "notes": 'Identify outdated material for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Automation: prioritize maintenance work',
        "notes": 'Prioritize maintenance work for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Automation: back up the current state',
        "notes": 'Back up the current state for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Automation: apply a focused improvement',
        "notes": 'Apply a focused improvement for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Automation: check existing behavior',
        "notes": 'Check existing behavior for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Automation: update supporting notes',
        "notes": 'Update supporting notes for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Automation: verify recovery steps',
        "notes": 'Verify recovery steps for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Automation: record maintenance changes',
        "notes": 'Record maintenance changes for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Automation: schedule the next review',
        "notes": 'Schedule the next review for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
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
