from app.database.models import User, Role, Post, Category
from flask_sqlalchemy import SQLAlchemy
from app import db, app
from werkzeug.security import check_password_hash
from flask import jsonify
import datetime
import jwt
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from werkzeug.security import generate_password_hash, check_password_hash

s = URLSafeTimedSerializer(app.config["SECRET_KEY"])
mail = Mail(app)


def create_new_user(data):
    print(data["username"])
    role = Role.query.filter_by(id=1).first()
    hashed_password = generate_password_hash(data["password"], method="sha256")
    user = User(username=data["username"], email=data["email"],
                password=hashed_password, role=role)
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
        token = jwt.encode(
            data, app.config["SECRET_KEY"], "HS256").decode("utf-8")
        return jsonify({"token": token})
    else:
        return None, 401


def send_link_to_email(data):
    print(data)
    print(data["email"])
    if data["email"] and data["email"].strip():
        print("wpada")
        token = s.dumps(data["email"], salt="check_email")
        link = "http://localhost:8080/#/reset_password/" + token

        msg = Message("Link to reset password", sender="grzesupel@gmail.com",
                    recipients=["grzesieks@sparkbit.pl"])
        msg.body = link
        mail.send(msg)
        return "Email has been sent successfully", 250
    else:
        return None, 400


def reset_password(data):
    try:
        email = s.loads(data["token"], salt="check_email", max_age=120)
        user = User.query.filter_by(email=email).first()
        hashed_password = generate_password_hash(
            data["password"], method="sha256")
        user.password = hashed_password
        db.session.add(user)
        db.session.commit()
    except SignatureExpired:
        return jsonify({"message": "Token is expired!"})
