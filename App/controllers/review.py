from App.models import Review
from App.database import db

def create_review(student, title, text):
    newReview = Review(title=title, text=text)
    student.reviews.append(newReview)
    db.session.add(student)
    db.session.commit()
    return newReview
    
def get_review(student):
    return Review.query.filter_by(student_id=student.id).first()

def get_all_reviews(students):
    for x in students:
        print(x.reviews)
        print('\n')
