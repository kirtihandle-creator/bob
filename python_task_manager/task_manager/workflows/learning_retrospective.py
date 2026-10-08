from datetime import date, timedelta
WORKFLOW_ID = 'learning_retrospective'
NAME = 'Learning program: Retrospective'
CATEGORY = 'learning'
PHASE = 'retrospective'
TASKS = (
    {
        "title": 'Learning program: collect outcome measures',
        "notes": 'Collect outcome measures for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Learning program: compare results with goals',
        "notes": 'Compare results with goals for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Learning program: review the project timeline',
        "notes": 'Review the project timeline for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Learning program: identify successful practices',
        "notes": 'Identify successful practices for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Learning program: identify recurring obstacles',
        "notes": 'Identify recurring obstacles for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Learning program: review effort estimates',
        "notes": 'Review effort estimates for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Learning program: collect participant feedback',
        "notes": 'Collect participant feedback for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Learning program: document surprising findings',
        "notes": 'Document surprising findings for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Learning program: choose process improvements',
        "notes": 'Choose process improvements for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Learning program: assign follow-up actions',
        "notes": 'Assign follow-up actions for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Learning program: archive useful materials',
        "notes": 'Archive useful materials for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Learning program: write the retrospective summary',
        "notes": 'Write the retrospective summary for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
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
