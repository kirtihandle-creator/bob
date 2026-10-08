from datetime import date, timedelta
WORKFLOW_ID = 'portfolio_retrospective'
NAME = 'Portfolio project: Retrospective'
CATEGORY = 'portfolio'
PHASE = 'retrospective'
TASKS = (
    {
        "title": 'Portfolio project: collect outcome measures',
        "notes": 'Collect outcome measures for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Portfolio project: compare results with goals',
        "notes": 'Compare results with goals for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Portfolio project: review the project timeline',
        "notes": 'Review the project timeline for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Portfolio project: identify successful practices',
        "notes": 'Identify successful practices for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Portfolio project: identify recurring obstacles',
        "notes": 'Identify recurring obstacles for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Portfolio project: review effort estimates',
        "notes": 'Review effort estimates for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Portfolio project: collect participant feedback',
        "notes": 'Collect participant feedback for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Portfolio project: document surprising findings',
        "notes": 'Document surprising findings for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Portfolio project: choose process improvements',
        "notes": 'Choose process improvements for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Portfolio project: assign follow-up actions',
        "notes": 'Assign follow-up actions for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Portfolio project: archive useful materials',
        "notes": 'Archive useful materials for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Portfolio project: write the retrospective summary',
        "notes": 'Write the retrospective summary for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
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
