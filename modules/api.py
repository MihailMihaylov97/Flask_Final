from flask import Blueprint
from flask_restful import Api, Resource


auth = Blueprint("auth_controller", __name__)
auth_api=Api(auth)


class Sign (param):
    def get(self):
        if param = "Test":
            return {"msg" : "Success"}, 200
        else:
            return {"msg" : "Fail"}, 403
    def post(self):
        global web
        return web         

class User():
    def post(self):
        pass
    def get(self):
        pass
        




auth_api.add_resource(Sign, "/sign/")
auth_api.add_resource(User, "user")