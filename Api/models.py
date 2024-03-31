from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    medical_images = db.relationship('MedicalImage')

class MedicalImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String(1000), unique=True)
    uploaded_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()
