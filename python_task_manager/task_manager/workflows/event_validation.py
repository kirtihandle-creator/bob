from datetime import date, timedelta
WORKFLOW_ID = 'event_validation'
NAME = 'Event project: Validation'
CATEGORY = 'event'
PHASE = 'validation'
TASKS = (
    {
        "title": 'Event project: define acceptance checks',
        "notes": 'Define acceptance checks for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Event project: prepare realistic examples',
        "notes": 'Prepare realistic examples for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Event project: check the normal workflow',
        "notes": 'Check the normal workflow for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Event project: check empty inputs',
        "notes": 'Check empty inputs for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Event project: check invalid inputs',
        "notes": 'Check invalid inputs for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Event project: check boundary conditions',
        "notes": 'Check boundary conditions for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Event project: check repeatability',
        "notes": 'Check repeatability for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Event project: check recovery behavior',
        "notes": 'Check recovery behavior for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Event project: review clarity of feedback',
        "notes": 'Review clarity of feedback for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Event project: record discovered issues',
        "notes": 'Record discovered issues for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Event project: verify corrections',
        "notes": 'Verify corrections for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Event project: summarize validation results',
        "notes": 'Summarize validation results for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
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
