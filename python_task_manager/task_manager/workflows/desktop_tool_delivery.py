from datetime import date, timedelta
WORKFLOW_ID = 'desktop_tool_delivery'
NAME = 'Desktop tool: Delivery'
CATEGORY = 'desktop_tool'
PHASE = 'delivery'
TASKS = (
    {
        "title": 'Desktop tool: confirm delivery scope',
        "notes": 'Confirm delivery scope for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 0,
    },
    {
        "title": 'Desktop tool: check outstanding issues',
        "notes": 'Check outstanding issues for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 0,
    },
    {
        "title": 'Desktop tool: prepare final materials',
        "notes": 'Prepare final materials for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'High',
        "day_offset": 1,
    },
    {
        "title": 'Desktop tool: write usage instructions',
        "notes": 'Write usage instructions for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 1,
    },
    {
        "title": 'Desktop tool: document known limitations',
        "notes": 'Document known limitations for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Desktop tool: prepare a demonstration',
        "notes": 'Prepare a demonstration for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 2,
    },
    {
        "title": 'Desktop tool: check destination requirements',
        "notes": 'Check destination requirements for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Desktop tool: create a backup copy',
        "notes": 'Create a backup copy for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 3,
    },
    {
        "title": 'Desktop tool: verify the delivery package',
        "notes": 'Verify the delivery package for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Desktop tool: complete the handoff',
        "notes": 'Complete the handoff for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 4,
    },
    {
        "title": 'Desktop tool: confirm recipient access',
        "notes": 'Confirm recipient access for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
        "priority": 'Normal',
        "day_offset": 5,
    },
    {
        "title": 'Desktop tool: record the delivered version',
        "notes": 'Record the delivered version for the desktop tool. Focus on clear desktop interactions and local storage. Record the outcome and any follow-up needed in your task notes.',
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
