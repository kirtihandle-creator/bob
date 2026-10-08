from datetime import date, timedelta
WORKFLOW_ID = 'automation_planning'
NAME = 'Automation: Planning'
CATEGORY = 'automation'
PHASE = 'planning'
TASKS = (
    {
        "title": 'Automation: define the outcome',
        "notes": 'Define the outcome for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Automation: set success criteria',
        "notes": 'Set success criteria for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Automation: break down the work',
        "notes": 'Break down the work for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Automation: estimate task effort',
        "notes": 'Estimate task effort for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Automation: identify dependencies',
        "notes": 'Identify dependencies for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Automation: assign responsibilities',
        "notes": 'Assign responsibilities for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Automation: set milestones',
        "notes": 'Set milestones for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Automation: reserve review time',
        "notes": 'Reserve review time for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Automation: record delivery risks',
        "notes": 'Record delivery risks for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Automation: choose progress measures',
        "notes": 'Choose progress measures for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Automation: review the schedule',
        "notes": 'Review the schedule for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Automation: approve the working plan',
        "notes": 'Approve the working plan for the automation. Focus on repeatable jobs and recoverable failures. Record the outcome and any follow-up needed in your task notes.',
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
