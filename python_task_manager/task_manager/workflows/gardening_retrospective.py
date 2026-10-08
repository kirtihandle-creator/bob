from datetime import date, timedelta
WORKFLOW_ID = 'gardening_retrospective'
NAME = 'Gardening project: Retrospective'
CATEGORY = 'gardening'
PHASE = 'retrospective'
TASKS = (
    {
        "title": 'Gardening project: collect outcome measures',
        "notes": 'Collect outcome measures for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Gardening project: compare results with goals',
        "notes": 'Compare results with goals for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Gardening project: review the project timeline',
        "notes": 'Review the project timeline for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Gardening project: identify successful practices',
        "notes": 'Identify successful practices for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Gardening project: identify recurring obstacles',
        "notes": 'Identify recurring obstacles for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Gardening project: review effort estimates',
        "notes": 'Review effort estimates for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Gardening project: collect participant feedback',
        "notes": 'Collect participant feedback for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Gardening project: document surprising findings',
        "notes": 'Document surprising findings for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Gardening project: choose process improvements',
        "notes": 'Choose process improvements for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Gardening project: assign follow-up actions',
        "notes": 'Assign follow-up actions for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Gardening project: archive useful materials',
        "notes": 'Archive useful materials for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Gardening project: write the retrospective summary',
        "notes": 'Write the retrospective summary for the gardening project. Focus on plant needs, seasonal timing, and sustainable care. Record the outcome and any follow-up needed in your task notes.',
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
