from datetime import date, timedelta
WORKFLOW_ID = 'automation_validation'
NAME = 'Automation: Validation'
CATEGORY = 'automation'
PHASE = 'validation'
TASKS = (
    {
        "title": 'Automation: define acceptance checks',
        "notes": 'Define acceptance checks for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Automation: prepare realistic examples',
        "notes": 'Prepare realistic examples for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Automation: check the normal workflow',
        "notes": 'Check the normal workflow for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Automation: check empty inputs',
        "notes": 'Check empty inputs for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Automation: check invalid inputs',
        "notes": 'Check invalid inputs for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Automation: check boundary conditions',
        "notes": 'Check boundary conditions for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Automation: check repeatability',
        "notes": 'Check repeatability for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Automation: check recovery behavior',
        "notes": 'Check recovery behavior for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Automation: review clarity of feedback',
        "notes": 'Review clarity of feedback for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Automation: record discovered issues',
        "notes": 'Record discovered issues for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Automation: verify corrections',
        "notes": 'Verify corrections for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Automation: summarize validation results',
        "notes": 'Summarize validation results for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
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
