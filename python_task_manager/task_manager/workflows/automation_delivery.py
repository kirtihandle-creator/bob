from datetime import date, timedelta
WORKFLOW_ID = 'automation_delivery'
NAME = 'Automation: Delivery'
CATEGORY = 'automation'
PHASE = 'delivery'
TASKS = (
    {
        "title": 'Automation: confirm delivery scope',
        "notes": 'Confirm delivery scope for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Automation: check outstanding issues',
        "notes": 'Check outstanding issues for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Automation: prepare final materials',
        "notes": 'Prepare final materials for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Automation: write usage instructions',
        "notes": 'Write usage instructions for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Automation: document known limitations',
        "notes": 'Document known limitations for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Automation: prepare a demonstration',
        "notes": 'Prepare a demonstration for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Automation: check destination requirements',
        "notes": 'Check destination requirements for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Automation: create a backup copy',
        "notes": 'Create a backup copy for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Automation: verify the delivery package',
        "notes": 'Verify the delivery package for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Automation: complete the handoff',
        "notes": 'Complete the handoff for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Automation: confirm recipient access',
        "notes": 'Confirm recipient access for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Automation: record the delivered version',
        "notes": 'Record the delivered version for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
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
