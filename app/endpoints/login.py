def init_login(api, Resource):

    from app.serializers import login_model, token_model
    from app.controllers import login

    ns_login = api.namespace("login", description="Operations related to login")

    @ns_login.route("/")
    class Login(Resource):

        @api.expect(login_model)
        # @api.marshal_with(token_model, code=200)
        @api.response(200, "You are loggin!")
        @api.response(401, "Not authorized!")
        def post(self):
            # if "token" in login(api.payload):
            #     return login(api.payload), 200
            # else:
            #     return None, 401
            return login(api.payload)
