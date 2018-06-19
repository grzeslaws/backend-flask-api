from flask_restplus import reqparse

pagination_parser = reqparse.RequestParser()
pagination_parser.add_argument("page", type=int, default=1, help="Select page number")
pagination_parser.add_argument("per_page", type=int, default=10, choices=[2, 10, 20, 30, 40, 50], help="How many items schould be on the page?")
