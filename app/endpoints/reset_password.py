def reset_password(api, Resource):

    from app.serializers import send_email_model, reset_password_model
    from app.controllers import send_link_to_email, reset_password

    ns = api.namespace("email", description="Operations related to send email")

    @ns.route("/send_email")
    class SendEmail(Resource):

        @ns.expect(send_email_model)
        @ns.response(250, "Everything went well and your email was delivered to the recipient server")
        def post(self):
            return send_link_to_email(api.payload)
            

    @ns.route("/reset_password/")
    class ResetPassword(Resource):

        @ns.expect(reset_password_model)
        def post(self):

            reset_password(api.payload) 
            return None
