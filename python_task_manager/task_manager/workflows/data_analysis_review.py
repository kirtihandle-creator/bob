from datetime import date, timedelta
WORKFLOW_ID = 'data_analysis_review'
NAME = 'Data analysis: Review'
CATEGORY = 'data_analysis'
PHASE = 'review'
TASKS = (
    {
        "title": 'Data analysis: collect the current deliverables',
        "notes": 'Collect the current deliverables for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Data analysis: review the original goals',
        "notes": 'Review the original goals for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Data analysis: check completeness',
        "notes": 'Check completeness for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Data analysis: check internal consistency',
        "notes": 'Check internal consistency for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Data analysis: review supporting evidence',
        "notes": 'Review supporting evidence for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Data analysis: review usability',
        "notes": 'Review usability for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Data analysis: identify confusing sections',
        "notes": 'Identify confusing sections for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Data analysis: collect reviewer feedback',
        "notes": 'Collect reviewer feedback for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Data analysis: prioritize requested changes',
        "notes": 'Prioritize requested changes for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Data analysis: apply agreed changes',
        "notes": 'Apply agreed changes for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Data analysis: verify the revised work',
        "notes": 'Verify the revised work for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Data analysis: record review decisions',
        "notes": 'Record review decisions for the data analysis. Focus on reliable datasets and reproducible findings. Record the outcome and any follow-up needed in your task notes.',
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
