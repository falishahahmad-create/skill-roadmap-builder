
from urllib.parse import quote_plus

PHASES = [
    ("Foundations", "Learn the basics of"),
    ("Core Skills", "Go deeper into"),
    ("Practice", "Practice with real exercises in"),
    ("Final Project", "Build and polish a final project in"),
]


def _phase_index(day, total_days):
    progress = day / total_days
    if progress <= 0.30:
        return 0
    if progress <= 0.70:
        return 1
    if progress <= 0.90:
        return 2
    return 3


def _resources(topic):
    q = quote_plus(topic)
    return {
        "YouTube": f"https://www.youtube.com/results?search_query={q}+tutorial",
        "Google": f"https://www.google.com/search?q={q}+guide",
    }


def generate_plan(goal, days, hours, level):
    plan = []
    for day in range(1, days + 1):
        phase_name, verb = PHASES[_phase_index(day, days)]
        topic = f"{goal} {phase_name}"

        tasks = [
            f"Study: {verb} {goal} ({round(hours * 0.6, 1)} hrs)",
            f"Practice: apply what you learned ({round(hours * 0.4, 1)} hrs)",
        ]
        if level == "Beginner":
            tasks.append("Write down 3 key terms you learned today")

        mini_project = None
        if day == days:
            mini_project = f"Final project: build something complete that shows your {goal} skills"
        elif day % 5 == 0:
            mini_project = f"Mini-project: build something small using what you learned so far in {goal}"

        plan.append({
            "day": day,
            "phase": phase_name,
            "tasks": tasks,
            "resources": _resources(topic),
            "mini_project": mini_project,
            "done": False,
        })
    return plan
