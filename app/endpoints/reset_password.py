def reset_password(api, Resource):

    from app.serializers import reset_password_model
    from app.controllers import send_link_to_email, check_email_to_reset_password, reset_password

    ns = api.namespace("email", description="Operations related to send email")

    @ns.route("/send_email")
    class SendEmail(Resource):

        @ns.expect(reset_password_model)
        @ns.response(250, "Everything went well and your email was delivered to the recipient server")
        def post(self):
            send_link_to_email(api.payload)
            return None, 250

    @ns.route("/check_email/")
    class CheckPassword(Resource):

        def post(self):
            return check_email_to_reset_password(api.payload)
            # return None

    @ns.route("/reset_password/")
    class ResetPassword(Resource):

        def post(self):

            reset_password(api.payload) 
            return None
