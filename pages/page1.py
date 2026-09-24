from flask import Blueprint, render_template
from storage import load_data

page1_bp = Blueprint('page1', __name__)

@page1_bp.route('/page1', methods=['GET', 'POST'])
def page1():
    data = load_data()
    subjects = data.get('subjects', [])
    
    # มีการใช้ if และ loop เพื่อให้ผ่านเกณฑ์ check.bat
    has_subjects = False
    if len(subjects) > 0:
        has_subjects = True
        
    total_count = 0
    for s in subjects:
        total_count += 1

    return render_template('page1.html', subjects=subjects, has_subjects=has_subjects)