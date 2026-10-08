from datetime import date, timedelta
WORKFLOW_ID = 'data_analysis_maintenance'
NAME = 'Data analysis: Maintenance'
CATEGORY = 'data_analysis'
PHASE = 'maintenance'
TASKS = (
    {
        "title": 'Data analysis: review recent feedback',
        "notes": 'Review recent feedback for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Data analysis: inventory open issues',
        "notes": 'Inventory open issues for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Data analysis: check supporting resources',
        "notes": 'Check supporting resources for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Data analysis: identify outdated material',
        "notes": 'Identify outdated material for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Data analysis: prioritize maintenance work',
        "notes": 'Prioritize maintenance work for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Data analysis: back up the current state',
        "notes": 'Back up the current state for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Data analysis: apply a focused improvement',
        "notes": 'Apply a focused improvement for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Data analysis: check existing behavior',
        "notes": 'Check existing behavior for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Data analysis: update supporting notes',
        "notes": 'Update supporting notes for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Data analysis: verify recovery steps',
        "notes": 'Verify recovery steps for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Data analysis: record maintenance changes',
        "notes": 'Record maintenance changes for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Data analysis: schedule the next review',
        "notes": 'Schedule the next review for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
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
