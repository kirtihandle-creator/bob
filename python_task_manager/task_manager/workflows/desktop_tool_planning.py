from datetime import date, timedelta
WORKFLOW_ID = 'desktop_tool_planning'
NAME = 'Desktop tool: Planning'
CATEGORY = 'desktop_tool'
PHASE = 'planning'
TASKS = (
    {
        "title": 'Desktop tool: define the outcome',
        "notes": 'Define the outcome for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Desktop tool: set success criteria',
        "notes": 'Set success criteria for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Desktop tool: break down the work',
        "notes": 'Break down the work for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Desktop tool: estimate task effort',
        "notes": 'Estimate task effort for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Desktop tool: identify dependencies',
        "notes": 'Identify dependencies for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Desktop tool: assign responsibilities',
        "notes": 'Assign responsibilities for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Desktop tool: set milestones',
        "notes": 'Set milestones for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Desktop tool: reserve review time',
        "notes": 'Reserve review time for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Desktop tool: record delivery risks',
        "notes": 'Record delivery risks for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Desktop tool: choose progress measures',
        "notes": 'Choose progress measures for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Desktop tool: review the schedule',
        "notes": 'Review the schedule for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Desktop tool: approve the working plan',
        "notes": 'Approve the working plan for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
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
