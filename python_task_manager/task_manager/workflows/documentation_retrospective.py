from datetime import date, timedelta
WORKFLOW_ID = 'documentation_retrospective'
NAME = 'Documentation: Retrospective'
CATEGORY = 'documentation'
PHASE = 'retrospective'
TASKS = (
    {
        "title": 'Documentation: collect outcome measures',
        "notes": 'Collect outcome measures for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Documentation: compare results with goals',
        "notes": 'Compare results with goals for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Documentation: review the project timeline',
        "notes": 'Review the project timeline for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Documentation: identify successful practices',
        "notes": 'Identify successful practices for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Documentation: identify recurring obstacles',
        "notes": 'Identify recurring obstacles for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Documentation: review effort estimates',
        "notes": 'Review effort estimates for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Documentation: collect participant feedback',
        "notes": 'Collect participant feedback for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Documentation: document surprising findings',
        "notes": 'Document surprising findings for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Documentation: choose process improvements',
        "notes": 'Choose process improvements for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Documentation: assign follow-up actions',
        "notes": 'Assign follow-up actions for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Documentation: archive useful materials',
        "notes": 'Archive useful materials for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Documentation: write the retrospective summary',
        "notes": 'Write the retrospective summary for the documentation. Focus on accurate explanations and useful examples. Record the outcome and any follow-up needed in your task notes.',
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
