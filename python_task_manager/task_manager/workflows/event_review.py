from datetime import date, timedelta
WORKFLOW_ID = 'event_review'
NAME = 'Event project: Review'
CATEGORY = 'event'
PHASE = 'review'
TASKS = (
    {
        "title": 'Event project: collect the current deliverables',
        "notes": 'Collect the current deliverables for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Event project: review the original goals',
        "notes": 'Review the original goals for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Event project: check completeness',
        "notes": 'Check completeness for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Event project: check internal consistency',
        "notes": 'Check internal consistency for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Event project: review supporting evidence',
        "notes": 'Review supporting evidence for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Event project: review usability',
        "notes": 'Review usability for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Event project: identify confusing sections',
        "notes": 'Identify confusing sections for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Event project: collect reviewer feedback',
        "notes": 'Collect reviewer feedback for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Event project: prioritize requested changes',
        "notes": 'Prioritize requested changes for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Event project: apply agreed changes',
        "notes": 'Apply agreed changes for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Event project: verify the revised work',
        "notes": 'Verify the revised work for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Event project: record review decisions',
        "notes": 'Record review decisions for the event project. Focus on attendee experience, logistics, and clear schedules. Record the outcome and any follow-up needed in your task notes.',
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
