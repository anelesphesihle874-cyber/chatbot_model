from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()

class Programmes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_of_prog = db.Column(db.String, nullable=False, unique=True)
    mathematics = db.Column(db.String, nullable=False)
    physx = db.Column(db.String, nullable=False)
    english= db.Column(db.String, nullable=False)
    req_points = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)




class Learners(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name =db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False, )
    email = db.Column(db.String, nullable=False, unique=True)
    password= db.Column(db.String, nullable=False)
    confirm_password =db.Column(db.String, nullable=False)
    date_created= db.Column(db.DateTime, default=datetime.utcnow)

    def gen_password(self, password):
        self.password=generate_password_hash(password)

    def confirm_password(self, conf_pass):
        return self.password==conf_pass

        