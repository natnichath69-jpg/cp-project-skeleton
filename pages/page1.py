import json


def build():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            items = json.load(f)
    except Exception:
        items = []

    return {
        "items": items,
    }