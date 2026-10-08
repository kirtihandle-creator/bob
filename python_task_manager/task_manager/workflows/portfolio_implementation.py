from datetime import date, timedelta
WORKFLOW_ID = 'portfolio_implementation'
NAME = 'Portfolio project: Implementation'
CATEGORY = 'portfolio'
PHASE = 'implementation'
TASKS = (
    {
        "title": 'Portfolio project: select the first milestone',
        "notes": 'Select the first milestone for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Portfolio project: prepare the input material',
        "notes": 'Prepare the input material for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Portfolio project: build the core deliverable',
        "notes": 'Build the core deliverable for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Portfolio project: handle common variations',
        "notes": 'Handle common variations for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Portfolio project: handle missing inputs',
        "notes": 'Handle missing inputs for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Portfolio project: add useful feedback',
        "notes": 'Add useful feedback for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Portfolio project: connect the main components',
        "notes": 'Connect the main components for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Portfolio project: review naming and structure',
        "notes": 'Review naming and structure for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Portfolio project: remove duplicated work',
        "notes": 'Remove duplicated work for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Portfolio project: document key decisions',
        "notes": 'Document key decisions for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Portfolio project: run the main workflow',
        "notes": 'Run the main workflow for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Portfolio project: record remaining gaps',
        "notes": 'Record remaining gaps for the portfolio project. Focus on demonstrable work and clear project narratives. Record the outcome and any follow-up needed in your task notes.',
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
