import json
from models import Subject


def build():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            raw_data = json.load(f)
    except Exception:
        raw_data = []

    subjects = []
    total_credits = 0
    total_points = 0.0

    for item in raw_data:
        sub = Subject(
            subject=item.get("subject"),
            credit=item.get("credit", 0),
            grade=item.get("grade", "F"),
            semester=item.get("semester", 1),
            status=item.get("status", "กรอกแล้ว"),
        )
        subjects.append(sub)

        total_credits += int(sub.credit)
        total_points += sub.calculate_point()

    gpa = (total_points / total_credits) if total_credits > 0 else 0.0

    return {
        "subjects": subjects,
        "total_credits": total_credits,
        "gpa": round(gpa, 2),
    }