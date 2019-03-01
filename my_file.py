from flask import Flask 
from flask_restful import Api, Resource
from modules.api import auth
from web import web
from extensions import db
from resources.user_resource import UserRegistration

app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'this will be my secret key'


db.init_app(app)
@app.before_first_request
def create_tables():
    db.create_all()


api = Api(app)


api.add_resource(UserRegistration, '/user')

app.register_blueprint(auth, url_prefix="/api/v1/auth")
app.register_blueprint(web, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)