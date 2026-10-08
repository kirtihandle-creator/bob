from datetime import date, timedelta
WORKFLOW_ID = 'desktop_tool_implementation'
NAME = 'Desktop tool: Implementation'
CATEGORY = 'desktop_tool'
PHASE = 'implementation'
TASKS = (
    {
        "title": 'Desktop tool: select the first milestone',
        "notes": 'Select the first milestone for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Desktop tool: prepare the input material',
        "notes": 'Prepare the input material for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Desktop tool: build the core deliverable',
        "notes": 'Build the core deliverable for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Desktop tool: handle common variations',
        "notes": 'Handle common variations for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Desktop tool: handle missing inputs',
        "notes": 'Handle missing inputs for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Desktop tool: add useful feedback',
        "notes": 'Add useful feedback for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Desktop tool: connect the main components',
        "notes": 'Connect the main components for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Desktop tool: review naming and structure',
        "notes": 'Review naming and structure for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Desktop tool: remove duplicated work',
        "notes": 'Remove duplicated work for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Desktop tool: document key decisions',
        "notes": 'Document key decisions for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Desktop tool: run the main workflow',
        "notes": 'Run the main workflow for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Desktop tool: record remaining gaps',
        "notes": 'Record remaining gaps for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
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
