from datetime import date, timedelta
WORKFLOW_ID = 'learning_discovery'
NAME = 'Learning program: Discovery'
CATEGORY = 'learning'
PHASE = 'discovery'
TASKS = (
    {
        "title": 'Learning program: define the problem',
        "notes": 'Define the problem for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Learning program: identify the audience',
        "notes": 'Identify the audience for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Learning program: collect existing examples',
        "notes": 'Collect existing examples for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Learning program: record user needs',
        "notes": 'Record user needs for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Learning program: list constraints',
        "notes": 'List constraints for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Learning program: review available resources',
        "notes": 'Review available resources for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Learning program: document assumptions',
        "notes": 'Document assumptions for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Learning program: identify unknowns',
        "notes": 'Identify unknowns for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Learning program: compare possible approaches',
        "notes": 'Compare possible approaches for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Learning program: prioritize opportunities',
        "notes": 'Prioritize opportunities for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Learning program: summarize findings',
        "notes": 'Summarize findings for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Learning program: confirm the project brief',
        "notes": 'Confirm the project brief for the learning program. Focus on practical exercises and measurable learning outcomes. Record the outcome and any follow-up needed in your task notes.',
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
