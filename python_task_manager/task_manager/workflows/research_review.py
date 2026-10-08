from datetime import date, timedelta
WORKFLOW_ID = 'research_review'
NAME = 'Research project: Review'
CATEGORY = 'research'
PHASE = 'review'
TASKS = (
    {
        "title": 'Research project: collect the current deliverables',
        "notes": 'Collect the current deliverables for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Research project: review the original goals',
        "notes": 'Review the original goals for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Research project: check completeness',
        "notes": 'Check completeness for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Research project: check internal consistency',
        "notes": 'Check internal consistency for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Research project: review supporting evidence',
        "notes": 'Review supporting evidence for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Research project: review usability',
        "notes": 'Review usability for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Research project: identify confusing sections',
        "notes": 'Identify confusing sections for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Research project: collect reviewer feedback',
        "notes": 'Collect reviewer feedback for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Research project: prioritize requested changes',
        "notes": 'Prioritize requested changes for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Research project: apply agreed changes',
        "notes": 'Apply agreed changes for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Research project: verify the revised work',
        "notes": 'Verify the revised work for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Research project: record review decisions',
        "notes": 'Record review decisions for the research project. Focus on traceable evidence and testable questions. Record the outcome and any follow-up needed in your task notes.',
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
