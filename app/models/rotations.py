from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash

class Rotation(db.Model):
    __tablename__ = 'rotations'

    if environment == "production" :
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    job_id = db.Column(db.Integer,  db.ForeignKey(add_prefix_for_prod("jobs.id")), nullable=False)

    rotation_user = db.relationship('User', back_populates="user_rotation")
    rotation_job = db.relationship('Job', back_populates="job_rotation")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'job_id': self.job_id
        }
