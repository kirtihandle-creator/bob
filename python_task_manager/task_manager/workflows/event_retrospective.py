from datetime import date, timedelta
WORKFLOW_ID = 'event_retrospective'
NAME = 'Event project: Retrospective'
CATEGORY = 'event'
PHASE = 'retrospective'
TASKS = (
    {
        "title": 'Event project: collect outcome measures',
        "notes": 'Collect outcome measures for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Event project: compare results with goals',
        "notes": 'Compare results with goals for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Event project: review the project timeline',
        "notes": 'Review the project timeline for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Event project: identify successful practices',
        "notes": 'Identify successful practices for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Event project: identify recurring obstacles',
        "notes": 'Identify recurring obstacles for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Event project: review effort estimates',
        "notes": 'Review effort estimates for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Event project: collect participant feedback',
        "notes": 'Collect participant feedback for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Event project: document surprising findings',
        "notes": 'Document surprising findings for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Event project: choose process improvements',
        "notes": 'Choose process improvements for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Event project: assign follow-up actions',
        "notes": 'Assign follow-up actions for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Event project: archive useful materials',
        "notes": 'Archive useful materials for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Event project: write the retrospective summary',
        "notes": 'Write the retrospective summary for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
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
