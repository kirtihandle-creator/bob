from datetime import date, timedelta
WORKFLOW_ID = 'data_analysis_discovery'
NAME = 'Data analysis: Discovery'
CATEGORY = 'data_analysis'
PHASE = 'discovery'
TASKS = (
    {
        "title": 'Data analysis: define the problem',
        "notes": 'Define the problem for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Data analysis: identify the audience',
        "notes": 'Identify the audience for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Data analysis: collect existing examples',
        "notes": 'Collect existing examples for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Data analysis: record user needs',
        "notes": 'Record user needs for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Data analysis: list constraints',
        "notes": 'List constraints for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Data analysis: review available resources',
        "notes": 'Review available resources for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Data analysis: document assumptions',
        "notes": 'Document assumptions for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Data analysis: identify unknowns',
        "notes": 'Identify unknowns for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Data analysis: compare possible approaches',
        "notes": 'Compare possible approaches for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Data analysis: prioritize opportunities',
        "notes": 'Prioritize opportunities for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Data analysis: summarize findings',
        "notes": 'Summarize findings for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Data analysis: confirm the project brief',
        "notes": 'Confirm the project brief for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
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
