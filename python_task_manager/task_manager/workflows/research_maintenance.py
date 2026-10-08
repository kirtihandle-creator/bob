from datetime import date, timedelta
WORKFLOW_ID = 'research_maintenance'
NAME = 'Research project: Maintenance'
CATEGORY = 'research'
PHASE = 'maintenance'
TASKS = (
    {
        "title": 'Research project: review recent feedback',
        "notes": 'Review recent feedback for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Research project: inventory open issues',
        "notes": 'Inventory open issues for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Research project: check supporting resources',
        "notes": 'Check supporting resources for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Research project: identify outdated material',
        "notes": 'Identify outdated material for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Research project: prioritize maintenance work',
        "notes": 'Prioritize maintenance work for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Research project: back up the current state',
        "notes": 'Back up the current state for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Research project: apply a focused improvement',
        "notes": 'Apply a focused improvement for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Research project: check existing behavior',
        "notes": 'Check existing behavior for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Research project: update supporting notes',
        "notes": 'Update supporting notes for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Research project: verify recovery steps',
        "notes": 'Verify recovery steps for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Research project: record maintenance changes',
        "notes": 'Record maintenance changes for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Research project: schedule the next review',
        "notes": 'Schedule the next review for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
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
