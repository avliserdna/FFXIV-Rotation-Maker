from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash


class Jobs(db.Model):
    __tablename__ = 'jobs'

    if environment =="production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(40), nullable=False, unique=True)
    abbreviation = db.Column(db.String(10), nullable =False, unique=True)
    role = db.Column(db.String(30), nullable =False, unique = True)

    job_rotation = db.relationship('Rotation', back_populates='rotation_job', cascade="all, delete")
    job_ability = db.relationship('Ability', back_populates="ability_job")

    def to_dict(self):
        return {
            'id': self.id,
            'job_name': self.job_name,
            'abbreviation': self.abbreviation,
            'role': self.role
        }
