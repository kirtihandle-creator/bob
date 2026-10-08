from datetime import date, timedelta
WORKFLOW_ID = 'data_analysis_validation'
NAME = 'Data analysis: Validation'
CATEGORY = 'data_analysis'
PHASE = 'validation'
TASKS = (
    {
        "title": 'Data analysis: define acceptance checks',
        "notes": 'Define acceptance checks for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Data analysis: prepare realistic examples',
        "notes": 'Prepare realistic examples for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Data analysis: check the normal workflow',
        "notes": 'Check the normal workflow for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Data analysis: check empty inputs',
        "notes": 'Check empty inputs for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Data analysis: check invalid inputs',
        "notes": 'Check invalid inputs for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Data analysis: check boundary conditions',
        "notes": 'Check boundary conditions for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Data analysis: check repeatability',
        "notes": 'Check repeatability for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Data analysis: check recovery behavior',
        "notes": 'Check recovery behavior for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Data analysis: review clarity of feedback',
        "notes": 'Review clarity of feedback for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Data analysis: record discovered issues',
        "notes": 'Record discovered issues for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Data analysis: verify corrections',
        "notes": 'Verify corrections for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Data analysis: summarize validation results',
        "notes": 'Summarize validation results for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
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
