from flask import Blueprint, render_template
from storage import load_data

page1_bp = Blueprint('page1', __name__)

@page1_bp.route('/page1', methods=['GET', 'POST'])
def page1():
    data = load_data()
    subjects = data.get('subjects', [])
    
    has_subjects = False
    if len(subjects) > 0:
        has_subjects = True
        
    for s in subjects:
        pass

    return render_template('page1.html', subjects=subjects, has_subjects=has_subjects)