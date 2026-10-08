from datetime import date, timedelta
WORKFLOW_ID = 'community_retrospective'
NAME = 'Community project: Retrospective'
CATEGORY = 'community'
PHASE = 'retrospective'
TASKS = (
    {
        "title": 'Community project: collect outcome measures',
        "notes": 'Collect outcome measures for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Community project: compare results with goals',
        "notes": 'Compare results with goals for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Community project: review the project timeline',
        "notes": 'Review the project timeline for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Community project: identify successful practices',
        "notes": 'Identify successful practices for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Community project: identify recurring obstacles',
        "notes": 'Identify recurring obstacles for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Community project: review effort estimates',
        "notes": 'Review effort estimates for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Community project: collect participant feedback',
        "notes": 'Collect participant feedback for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Community project: document surprising findings',
        "notes": 'Document surprising findings for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Community project: choose process improvements',
        "notes": 'Choose process improvements for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Community project: assign follow-up actions',
        "notes": 'Assign follow-up actions for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Community project: archive useful materials',
        "notes": 'Archive useful materials for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Community project: write the retrospective summary',
        "notes": 'Write the retrospective summary for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
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
