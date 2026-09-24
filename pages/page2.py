import json
from flask import redirect, request, url_for


def build():
    if request.method == "POST":
        subject = request.form.get("subject")
        credit = request.form.get("credit")
        grade = request.form.get("grade")
        semester = request.form.get("semester")

        if subject and credit and grade and semester:
            new_item = {
                "subject": subject,
                "credit": int(credit),
                "grade": grade,
                "semester": int(semester),
                "status": "กรอกแล้ว",
            }
            try:
                with open("data.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = []

            data.append(new_item)

            with open("data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            return redirect(url_for("page2"))

    return {}