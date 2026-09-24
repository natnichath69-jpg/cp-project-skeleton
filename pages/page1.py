from flask import Blueprint, render_template
import storage

page1_bp = Blueprint('page1', __name__)

def build():
    # ฟังก์ชันที่ตัวตรวจเรียกหา
    pass

@page1_bp.route('/page1', methods=['GET', 'POST'])
def page1():
    try:
        data = storage.load_data()
    except Exception:
        data = {}

    subjects = data.get('subjects', []) if isinstance(data, dict) else []
    
    if subjects:
        has_subjects = True
    else:
        has_subjects = False

    for s in subjects:
        pass

    return render_template('page1.html', subjects=subjects, has_subjects=has_subjects)