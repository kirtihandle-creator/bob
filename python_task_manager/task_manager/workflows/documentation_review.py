from datetime import date, timedelta
WORKFLOW_ID = 'documentation_review'
NAME = 'Documentation: Review'
CATEGORY = 'documentation'
PHASE = 'review'
TASKS = (
    {
        "title": 'Documentation: collect the current deliverables',
        "notes": 'Collect the current deliverables for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Documentation: review the original goals',
        "notes": 'Review the original goals for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Documentation: check completeness',
        "notes": 'Check completeness for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Documentation: check internal consistency',
        "notes": 'Check internal consistency for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Documentation: review supporting evidence',
        "notes": 'Review supporting evidence for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Documentation: review usability',
        "notes": 'Review usability for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Documentation: identify confusing sections',
        "notes": 'Identify confusing sections for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Documentation: collect reviewer feedback',
        "notes": 'Collect reviewer feedback for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Documentation: prioritize requested changes',
        "notes": 'Prioritize requested changes for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Documentation: apply agreed changes',
        "notes": 'Apply agreed changes for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Documentation: verify the revised work',
        "notes": 'Verify the revised work for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Documentation: record review decisions',
        "notes": 'Record review decisions for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
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
