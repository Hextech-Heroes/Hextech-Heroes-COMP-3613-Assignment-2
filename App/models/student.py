from App.database import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fName = db.Column(db.String(80), unique=True, nullable=False)
    lName = db.Column(db.String(80), unique=True, nullable=False)
    reviews = db.relationship('Review', backref='student', lazy=True, cascade="all, delete-orphan")

    def __init__(self, fName, lName):
      self.fName = fName
      self.lName = lName

    def __repr__(self):
      return f'<Student {self.id} - {self.fName} {self.lName}>'
    
    def get_json(self) -> dict[str, str]:
        return {
            "id": self.id,
            "first_name": self.fName,
            "last_name": self.lName,
        }