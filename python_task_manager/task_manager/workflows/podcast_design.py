from datetime import date, timedelta
WORKFLOW_ID = 'podcast_design'
NAME = 'Podcast project: Design'
CATEGORY = 'podcast'
PHASE = 'design'
TASKS = (
    {
        "title": 'Podcast project: review requirements',
        "notes": 'Review requirements for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Podcast project: sketch the structure',
        "notes": 'Sketch the structure for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Podcast project: describe the main flow',
        "notes": 'Describe the main flow for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Podcast project: define inputs',
        "notes": 'Define inputs for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Podcast project: define outputs',
        "notes": 'Define outputs for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Podcast project: choose naming conventions',
        "notes": 'Choose naming conventions for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Podcast project: design error handling',
        "notes": 'Design error handling for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Podcast project: check accessibility needs',
        "notes": 'Check accessibility needs for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Podcast project: create an example',
        "notes": 'Create an example for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Podcast project: compare design options',
        "notes": 'Compare design options for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Podcast project: review design decisions',
        "notes": 'Review design decisions for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Podcast project: finalize the design notes',
        "notes": 'Finalize the design notes for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
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
