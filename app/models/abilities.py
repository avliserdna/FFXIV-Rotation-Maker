from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Ability(db.Model):
    __tablename__ = "abilities"

    if environment == "production":
        __table_args__ = {'schema':SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("jobs.id")), nullable=False)
    ability_name = db.Column(db.String(255), nullable=False)
    isGCD = db.Column(db.Boolean, default = False, nullable = False)
    isOGCD = db.Column(db.Boolean, default = False, nullable = False)
    cooldown = db.Column(db.Numeric, nullable=False)

    ability_job = db.relationship('Job', back_populates="job_ability")
    def to_dict(self):
        return {
            'id': self.id,
            'job_id': self.job_id,
            'ability_name': self.ability_name,
            'isGCD': self.isGCD,
            'isOGCD': self.isOGCD,
            'cooldown': self.cooldown
        }
