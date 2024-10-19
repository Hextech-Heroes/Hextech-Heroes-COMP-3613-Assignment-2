from App.models import Student
from App.database import db

def create_student(fName, lName):
    newStudent = Student(fName=fName, lName=lName)
    db.session.add(newStudent)
    db.session.commit()
    return newStudent

def get_student_by_lName(lName):
    return Student.query.filter_by(lName=lName).first()

def get_student(id):
    return Student.query.get(id)

def get_all_students():
    return Student.query.all()
    
def get_all_students_json():
    students = Student.query.all()
    if not students:
        return []
    students = [student.get_json() for student in students]
    return students
