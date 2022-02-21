from db.HomeworksEntity import HomeworkEntity
from app import db

mock_data = []


def fetch_homeworks():
    return db.session.query(HomeworkEntity)
