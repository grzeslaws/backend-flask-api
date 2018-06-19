def init_login(api, Resource):

    from app.serializers import login_model
    from app.controllers import login

    ns_login = api.namespace("login", description="Operations related to login")

    @ns_login.route("/")
    class Login(Resource):

        @api.expect(login_model)
        @api.response(200, "You are loggin!")
        @api.response(401, "Not authorized!")
        def post(self):
            return login(api.payload)
