def init_user(api, pagination_parser, Resource, request, token_required):

    from app.serializers import user_model_list, user_model
    from app.database.models import User
    from app.controllers import create_new_user, edit_user, delete_user

    ns_user = api.namespace("user", description="Operations related to user")

    @ns_user.route("/")
    class UserList(Resource):

        @api.expect(pagination_parser)
        @ns_user.marshal_with(user_model_list)
        @token_required
        def get(current_user, self):
            args = pagination_parser.parse_args(request)
            users = User.query.paginate(
                args.get("page", 1), args.get("per_page", 7), error_out=False)
            return users

        @api.expect(user_model)
        def post(self):
            create_new_user(api.payload)
            return None, 201

    @ns_user.route("/<int:id>")
    @api.response(404, "Page not found!")
    class UserOne(Resource):

        @api.expect(user_model)
        @api.response(204, "User has been updated!")
        def put(self, id):
            edit_user(id, api.payload)
            return None, 204

        @api.response(204, "User was deleted!")
        def delete(self, id):
            delete_user(id)
            return None, 204
