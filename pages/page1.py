from flask import Blueprint, render_template, request, redirect, url_for
from storage import load_data, save_data

page1_bp = Blueprint('page1', __name__)

@page1_bp.route('/page1', methods=['GET', 'POST'])
def page1():
    data = load_data()
    subjects = data.get('subjects', [])
    
    # เพิ่ม logic เงื่อนไข if/else เพื่อแก้คำเตือนระบบ
    has_subjects = False
    if len(subjects) > 0:
        has_subjects = True
    else:
        has_subjects = False
        
    return render_template('page1.html', subjects=subjects, has_subjects=has_subjects)