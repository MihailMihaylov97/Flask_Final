from flask_restful import Resource, reqparse
from models.models import UserModel

parser = reqparse.RequestParser()
parser.add_argument(
    'username', help='This field cannot be blank', required=True)
parser.add_argument(
    'password', help='This field cannot be blank', required=True)
parser.add_argument(
    'name', help='This field cannot be blank', required=True)
parser.add_argument(
    'email', help='This field cannot be blank', required=True)



class UserRegistration(Resource):

    def post(self):
        data = parser.parse_args()
        new_user = UserModel(
            username=data['username'],
            password=data['password'],
            name=data['name'],
            email=data['email']
        )
        try:
            new_user.save_to_db()
            return {
                'message': 'User {} was created'.format(data['username'])
            }
        except None:
    def get(self):
        pass
return {'message': 'Something went wrong'}, 500