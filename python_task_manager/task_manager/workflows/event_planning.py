from datetime import date, timedelta
WORKFLOW_ID = 'event_planning'
NAME = 'Event project: Planning'
CATEGORY = 'event'
PHASE = 'planning'
TASKS = (
    {
        "title": 'Event project: define the outcome',
        "notes": 'Define the outcome for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Event project: set success criteria',
        "notes": 'Set success criteria for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Event project: break down the work',
        "notes": 'Break down the work for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Event project: estimate task effort',
        "notes": 'Estimate task effort for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Event project: identify dependencies',
        "notes": 'Identify dependencies for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Event project: assign responsibilities',
        "notes": 'Assign responsibilities for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Event project: set milestones',
        "notes": 'Set milestones for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Event project: reserve review time',
        "notes": 'Reserve review time for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Event project: record delivery risks',
        "notes": 'Record delivery risks for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Event project: choose progress measures',
        "notes": 'Choose progress measures for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Event project: review the schedule',
        "notes": 'Review the schedule for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Event project: approve the working plan',
        "notes": 'Approve the working plan for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
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
