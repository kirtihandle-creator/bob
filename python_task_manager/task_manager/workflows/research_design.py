from datetime import date, timedelta
WORKFLOW_ID = 'research_design'
NAME = 'Research project: Design'
CATEGORY = 'research'
PHASE = 'design'
TASKS = (
    {
        "title": 'Research project: review requirements',
        "notes": 'Review requirements for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Research project: sketch the structure',
        "notes": 'Sketch the structure for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Research project: describe the main flow',
        "notes": 'Describe the main flow for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Research project: define inputs',
        "notes": 'Define inputs for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Research project: define outputs',
        "notes": 'Define outputs for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Research project: choose naming conventions',
        "notes": 'Choose naming conventions for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Research project: design error handling',
        "notes": 'Design error handling for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Research project: check accessibility needs',
        "notes": 'Check accessibility needs for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Research project: create an example',
        "notes": 'Create an example for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Research project: compare design options',
        "notes": 'Compare design options for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Research project: review design decisions',
        "notes": 'Review design decisions for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Research project: finalize the design notes',
        "notes": 'Finalize the design notes for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
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
