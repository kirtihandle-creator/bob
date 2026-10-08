from datetime import date, timedelta
WORKFLOW_ID = 'community_design'
NAME = 'Community project: Design'
CATEGORY = 'community'
PHASE = 'design'
TASKS = (
    {
        "title": 'Community project: review requirements',
        "notes": 'Review requirements for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Community project: sketch the structure',
        "notes": 'Sketch the structure for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Community project: describe the main flow',
        "notes": 'Describe the main flow for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Community project: define inputs',
        "notes": 'Define inputs for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Community project: define outputs',
        "notes": 'Define outputs for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Community project: choose naming conventions',
        "notes": 'Choose naming conventions for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Community project: design error handling',
        "notes": 'Design error handling for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Community project: check accessibility needs',
        "notes": 'Check accessibility needs for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Community project: create an example',
        "notes": 'Create an example for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Community project: compare design options',
        "notes": 'Compare design options for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Community project: review design decisions',
        "notes": 'Review design decisions for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Community project: finalize the design notes',
        "notes": 'Finalize the design notes for the community project. Focus on participant needs and accessible activities. Record the outcome and any follow-up needed in your task notes.',
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
