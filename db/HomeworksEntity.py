from app import db


class HomeworkEntity(db.Model):
    __tablename__ = 'Homeworks'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255))
    date = db.Column(db.DateTime())
    description = db.Column(db.Text())

    def __init__(self, subject, date, description):
        self.subject = subject
        self.date = date
        self.description = description
