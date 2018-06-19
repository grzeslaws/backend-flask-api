import jwt
from flask import request, url_for, jsonify
from flask_restplus import Resource
from functools import wraps
from app import api, app
from ..database.models import User
from app.parsers import pagination_parser
from ..endpoints.post import init_post
from ..endpoints.user import init_user
from ..endpoints.login import init_login
from ..endpoints.reset_password import reset_password


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        print("token")

        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        if not token:
            return {"message": "Token is missing!"}, 401
        try:
            data = jwt.decode(
                token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.filter_by(
                id=data["id"]).first()
        except:
            {"message": "Token is invalid!"}, 401

        return f(current_user, *args, **kwargs)

    return decorated


init_post(api, pagination_parser, Resource, request, token_required)
init_user(api, pagination_parser, Resource, request, token_required)
reset_password(api, Resource)
init_login(api, Resource)
