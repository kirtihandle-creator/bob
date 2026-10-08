from datetime import date, timedelta
WORKFLOW_ID = 'podcast_planning'
NAME = 'Podcast project: Planning'
CATEGORY = 'podcast'
PHASE = 'planning'
TASKS = (
    {
        "title": 'Podcast project: define the outcome',
        "notes": 'Define the outcome for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Podcast project: set success criteria',
        "notes": 'Set success criteria for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Podcast project: break down the work',
        "notes": 'Break down the work for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Podcast project: estimate task effort',
        "notes": 'Estimate task effort for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Podcast project: identify dependencies',
        "notes": 'Identify dependencies for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Podcast project: assign responsibilities',
        "notes": 'Assign responsibilities for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Podcast project: set milestones',
        "notes": 'Set milestones for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Podcast project: reserve review time',
        "notes": 'Reserve review time for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Podcast project: record delivery risks',
        "notes": 'Record delivery risks for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Podcast project: choose progress measures',
        "notes": 'Choose progress measures for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Podcast project: review the schedule',
        "notes": 'Review the schedule for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Podcast project: approve the working plan',
        "notes": 'Approve the working plan for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
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
