from datetime import date, timedelta
WORKFLOW_ID = 'data_analysis_retrospective'
NAME = 'Data analysis: Retrospective'
CATEGORY = 'data_analysis'
PHASE = 'retrospective'
TASKS = (
    {
        "title": 'Data analysis: collect outcome measures',
        "notes": 'Collect outcome measures for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Data analysis: compare results with goals',
        "notes": 'Compare results with goals for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Data analysis: review the project timeline',
        "notes": 'Review the project timeline for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Data analysis: identify successful practices',
        "notes": 'Identify successful practices for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Data analysis: identify recurring obstacles',
        "notes": 'Identify recurring obstacles for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Data analysis: review effort estimates',
        "notes": 'Review effort estimates for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Data analysis: collect participant feedback',
        "notes": 'Collect participant feedback for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Data analysis: document surprising findings',
        "notes": 'Document surprising findings for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Data analysis: choose process improvements',
        "notes": 'Choose process improvements for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Data analysis: assign follow-up actions',
        "notes": 'Assign follow-up actions for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Data analysis: archive useful materials',
        "notes": 'Archive useful materials for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Data analysis: write the retrospective summary',
        "notes": 'Write the retrospective summary for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
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
