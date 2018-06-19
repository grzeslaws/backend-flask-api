from app.database.models import User, Role, Post, Category
from flask_sqlalchemy import SQLAlchemy
from app import db, app
from werkzeug.security import check_password_hash
from flask import jsonify
import datetime
import jwt


def create_new_user(data):
    print(data["username"])
    role = Role.query.filter_by(id=data["role_id"]).first()
    user = User(username=data["username"], email=data["email"], role=role)
    db.session.add(user)
    db.session.commit()


def edit_user(id, data):
    role = Role.query.filter_by(id=data["role_id"]).first()
    user = User.query.filter_by(id=id).first()
    user.username = data["username"]
    user.email = data["email"]
    user.role = role
    db.session.add(user)
    db.session.commit()


def delete_user(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()


def create_new_post(data):
    category = Category.query.filter_by(id=data["category_id"]).first()
    post = Post(title=data["title"], content=data["content"],
                author="tom 5", category=category)
    print(post)
    db.session.add(post)
    db.session.commit()


def edit_post(id, data):
    category = Category.query.filter_by(id=data["category_id"]).first()
    post = Post.query.filter_by(id=id).first()
    post.title = data["title"]
    post.content = data["content"]
    post.author = data["author"]
    post.category = category
    db.session.add(post)
    db.session.commit()


def get_post(id):
    return Post.query.filter_by(id=id).first()

def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    db.session.delete(post)
    db.session.commit()


def login(data):
    token = None
    user = User.query.filter_by(username=data["username"]).first()
    if (check_password_hash(user.password, data["password"])):
        data = {"id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=280)}
        token = jwt.encode(data, app.config["SECRET_KEY"], "HS256").decode("utf-8")
        return jsonify({"token": token}) 
