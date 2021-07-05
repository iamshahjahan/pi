from flask_restplus import Resource, abort

from docker_mysql_mongod_sqs_s3.src.user.user_controller import UserController


class UserResource(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self):
        pass

    def post(self):
        user_controller = UserController()
        user_controller.insert("shahjahan","ahmsjaha@gmail.com")
        user_controller.insert("ahsan","ahmsjfdasfdsaha@gmail.com")
