from datetime import date, timedelta
WORKFLOW_ID = 'documentation_discovery'
NAME = 'Documentation: Discovery'
CATEGORY = 'documentation'
PHASE = 'discovery'
TASKS = (
    {
        "title": 'Documentation: define the problem',
        "notes": 'Define the problem for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Documentation: identify the audience',
        "notes": 'Identify the audience for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Documentation: collect existing examples',
        "notes": 'Collect existing examples for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Documentation: record user needs',
        "notes": 'Record user needs for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Documentation: list constraints',
        "notes": 'List constraints for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Documentation: review available resources',
        "notes": 'Review available resources for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Documentation: document assumptions',
        "notes": 'Document assumptions for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Documentation: identify unknowns',
        "notes": 'Identify unknowns for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Documentation: compare possible approaches',
        "notes": 'Compare possible approaches for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Documentation: prioritize opportunities',
        "notes": 'Prioritize opportunities for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Documentation: summarize findings',
        "notes": 'Summarize findings for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Documentation: confirm the project brief',
        "notes": 'Confirm the project brief for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
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
