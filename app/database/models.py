from flask_sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(200))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"), nullable=False)
    role = db.relationship("Role", backref=db.backref("user", lazy=True))

    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50))

    def __repr__(self):
        return "Role {}".format(self.role)


class Post(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    author = db.Column(db.String(120))
    create_at = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", backref=db.backref("post", lazy=True))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(120))