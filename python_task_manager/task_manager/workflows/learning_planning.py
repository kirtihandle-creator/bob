from datetime import date, timedelta
WORKFLOW_ID = 'learning_planning'
NAME = 'Learning program: Planning'
CATEGORY = 'learning'
PHASE = 'planning'
TASKS = (
    {
        "title": 'Learning program: define the outcome',
        "notes": 'Define the outcome for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Learning program: set success criteria',
        "notes": 'Set success criteria for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Learning program: break down the work',
        "notes": 'Break down the work for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Learning program: estimate task effort',
        "notes": 'Estimate task effort for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Learning program: identify dependencies',
        "notes": 'Identify dependencies for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Learning program: assign responsibilities',
        "notes": 'Assign responsibilities for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Learning program: set milestones',
        "notes": 'Set milestones for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Learning program: reserve review time',
        "notes": 'Reserve review time for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Learning program: record delivery risks',
        "notes": 'Record delivery risks for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Learning program: choose progress measures',
        "notes": 'Choose progress measures for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Learning program: review the schedule',
        "notes": 'Review the schedule for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Learning program: approve the working plan',
        "notes": 'Approve the working plan for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
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
