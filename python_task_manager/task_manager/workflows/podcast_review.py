from datetime import date, timedelta
WORKFLOW_ID = 'podcast_review'
NAME = 'Podcast project: Review'
CATEGORY = 'podcast'
PHASE = 'review'
TASKS = (
    {
        "title": 'Podcast project: collect the current deliverables',
        "notes": 'Collect the current deliverables for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Podcast project: review the original goals',
        "notes": 'Review the original goals for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Podcast project: check completeness',
        "notes": 'Check completeness for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Podcast project: check internal consistency',
        "notes": 'Check internal consistency for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Podcast project: review supporting evidence',
        "notes": 'Review supporting evidence for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Podcast project: review usability',
        "notes": 'Review usability for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Podcast project: identify confusing sections',
        "notes": 'Identify confusing sections for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Podcast project: collect reviewer feedback',
        "notes": 'Collect reviewer feedback for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Podcast project: prioritize requested changes',
        "notes": 'Prioritize requested changes for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Podcast project: apply agreed changes',
        "notes": 'Apply agreed changes for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Podcast project: verify the revised work',
        "notes": 'Verify the revised work for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Podcast project: record review decisions',
        "notes": 'Record review decisions for the podcast project. Focus on episode structure, clear audio, and listener needs. Record the outcome and any follow-up needed in your task notes.',
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
