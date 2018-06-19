def init_post(api, pagination_parser, Resource, request, token_required):

    from app.serializers import post_model_list, post_model
    from app.database.models import Post
    from app.controllers import create_new_post, edit_post, delete_post, get_post

    ns_post = api.namespace("post", description="Operations related to post")

    @ns_post.route("/")
    class PostList(Resource):

        @api.expect(pagination_parser)
        @ns_post.marshal_with(post_model_list)
        def get(self):
            args = pagination_parser.parse_args(request)
            posts = Post.query.paginate(
                args.get("page", 1), args.get("per_page", 7), error_out=False)
            return posts

        @api.expect(post_model)
        def post(self):
            create_new_post(api.payload)
            return None, 201

    @ns_post.route("/<int:id>")
    @api.response(404, "Page not found!")
    class PostOne(Resource):

        @ns_post.marshal_with(post_model)
        @api.response(204, "Post has been updated!")
        def get(self, id):
            print(get_post(id))
            return get_post(id)

        @api.expect(post_model)
        @api.response(204, "Post has been updated!")
        def put(self, id):
            edit_post(id, api.payload)
            return None, 204

        @api.response(204, "Post has been deleted!")
        def delete(self, id):
            delete_post(id)
            return None, 204
