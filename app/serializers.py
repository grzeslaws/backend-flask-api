from flask_restplus import fields, Model
from app import api

pagination_model = api.model("A page of results", {
    "page": fields.Integer(description="Number of this page of results"),
    "pages": fields.Integer(description="Total number of pages of results"),
    "per_page": fields.Integer(description="Number of items per page of results"),
    "total": fields.Integer(description="Total number of results"),
    "has_prev": fields.Integer(description="Is prev page?"),
    "has_next": fields.Integer(description="Is next page?"),
})

user_model = api.model("user_model", {
    "id": fields.Integer,
    "username": fields.String(required=True, description="User name"),
    "email": fields.String(description="User email"),
    "password": fields.String(description="User password"),
    "role_id": fields.Integer,
    "role": fields.String(attributes="role.name"),
})

user_model_list = api.inherit("Page of blog posts", pagination_model,
                              {"items": fields.List(
                                  fields.Nested(user_model))},
                              )

post_model = api.model("post_model", {
    "id": fields.String,
    "title": fields.String(required=True),
    "content": fields.String,
    "author": fields.String,
    "create_at": fields.DateTime(dt_format='rfc822'),
    "category_id": fields.Integer,
    "category": fields.String(attributes="category.category_name")
})

category_model = api.model("category_model", {
    "id": fields.Integer,
    "category_name": fields.String
})

post_model_list = api.inherit("Page of posts", pagination_model,
                              {"items": fields.List(
                                  fields.Nested(post_model))},
                              )

login_model = api.model("login_model", {
    "username": fields.String(required=True),
    "password": fields.String(required=True)
})

token_model = api.model("token_model", {
    "token": fields.String
})
