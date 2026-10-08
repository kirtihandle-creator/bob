from datetime import date, timedelta
WORKFLOW_ID = 'desktop_tool_design'
NAME = 'Desktop tool: Design'
CATEGORY = 'desktop_tool'
PHASE = 'design'
TASKS = (
    {
        "title": 'Desktop tool: review requirements',
        "notes": 'Review requirements for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Desktop tool: sketch the structure',
        "notes": 'Sketch the structure for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Desktop tool: describe the main flow',
        "notes": 'Describe the main flow for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Desktop tool: define inputs',
        "notes": 'Define inputs for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Desktop tool: define outputs',
        "notes": 'Define outputs for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Desktop tool: choose naming conventions',
        "notes": 'Choose naming conventions for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Desktop tool: design error handling',
        "notes": 'Design error handling for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Desktop tool: check accessibility needs',
        "notes": 'Check accessibility needs for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Desktop tool: create an example',
        "notes": 'Create an example for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Desktop tool: compare design options',
        "notes": 'Compare design options for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Desktop tool: review design decisions',
        "notes": 'Review design decisions for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Desktop tool: finalize the design notes',
        "notes": 'Finalize the design notes for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
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
