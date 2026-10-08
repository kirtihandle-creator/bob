from datetime import date, timedelta
WORKFLOW_ID = 'content_delivery'
NAME = 'Content project: Delivery'
CATEGORY = 'content'
PHASE = 'delivery'
TASKS = (
    {
        "title": 'Content project: confirm delivery scope',
        "notes": 'Confirm delivery scope for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Content project: check outstanding issues',
        "notes": 'Check outstanding issues for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Content project: prepare final materials',
        "notes": 'Prepare final materials for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Content project: write usage instructions',
        "notes": 'Write usage instructions for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Content project: document known limitations',
        "notes": 'Document known limitations for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Content project: prepare a demonstration',
        "notes": 'Prepare a demonstration for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Content project: check destination requirements',
        "notes": 'Check destination requirements for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Content project: create a backup copy',
        "notes": 'Create a backup copy for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Content project: verify the delivery package',
        "notes": 'Verify the delivery package for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Content project: complete the handoff',
        "notes": 'Complete the handoff for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Content project: confirm recipient access',
        "notes": 'Confirm recipient access for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Content project: record the delivered version',
        "notes": 'Record the delivered version for the content project. Focus on audience needs and clear editorial standards. Record the outcome and any follow-up needed in your task notes.',
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
