from datetime import date, timedelta
WORKFLOW_ID = 'documentation_planning'
NAME = 'Documentation: Planning'
CATEGORY = 'documentation'
PHASE = 'planning'
TASKS = (
    {
        "title": 'Documentation: define the outcome',
        "notes": 'Define the outcome for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Documentation: set success criteria',
        "notes": 'Set success criteria for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Documentation: break down the work',
        "notes": 'Break down the work for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Documentation: estimate task effort',
        "notes": 'Estimate task effort for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Documentation: identify dependencies',
        "notes": 'Identify dependencies for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Documentation: assign responsibilities',
        "notes": 'Assign responsibilities for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Documentation: set milestones',
        "notes": 'Set milestones for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Documentation: reserve review time',
        "notes": 'Reserve review time for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Documentation: record delivery risks',
        "notes": 'Record delivery risks for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Documentation: choose progress measures',
        "notes": 'Choose progress measures for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Documentation: review the schedule',
        "notes": 'Review the schedule for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Documentation: approve the working plan',
        "notes": 'Approve the working plan for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
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
