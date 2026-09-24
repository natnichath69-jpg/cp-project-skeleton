"""models.py — Class สำหรับจัดการข้อมูลรายวิชา (GPA Calculator)"""


class Subject:
    def __init__(self, subject, credit, grade, semester, status="กรอกแล้ว"):
        self.subject = subject
        self.credit = credit
        self.grade = grade
        self.semester = semester
        self.status = status

    def calculate_point(self):
        """คำนวณคะแนนเกรดรวมของวิชานี้ (หน่วยกิต x คะแนนเกรด)"""
        grade_map = {
            "A": 4.0,
            "B+": 3.5,
            "B": 3.0,
            "C+": 2.5,
            "C": 2.0,
            "D+": 1.5,
            "D": 1.0,
            "F": 0.0,
        }
        point = grade_map.get(str(self.grade).upper(), 0.0)
        return float(self.credit) * point