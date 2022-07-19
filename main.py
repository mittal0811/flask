from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from sqlalchemy.dialects.mysql import MEDIUMINT, TINYINT


app = Flask(__name__)
CORS(app)


# Databse configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2lhAY7VaMpeSfT9jIoeY@containers-us-west-61.railway.app:7826/railway'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


ma = Marshmallow(app)


# user class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(45))
    lastname = db.Column(db.String(45))
    jobtitle = db.Column(db.String(45))
    phonenumber = db.Column(db.String(10))
    country = db.Column(TINYINT(unsigned=True))

    def __init__(self, firstname, lastname, jobtitle, phonenumber, country):
        self.firstname = firstname
        self.lastname = lastname
        self.jobtitle = jobtitle
        self.phonenumber = phonenumber
        self.country = country


class UserSchema(ma.Schema):
    class Meta:
        fields = ('firstname', 'lastname', 'jobtitle',
                  'phonenumber', 'country')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/')
def index():
    return jsonify({"hello": "Test version ssss"})


@app.route('/get', methods=['GET'])
def get_users_all():
    all_users = User.query.all()
    results = users_schema.dump(all_users)
    return jsonify(results)


@app.route('/get/<id>', methods=['GET'])
def post_details(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)

    user.firstname = request.json['firstname']
    user.lastname = request.json['lastname']
    user.jobtitle = request.json['jobtitle']
    user.phonenumber = request.json['phonenumber']
    user.country = request.json['country']

    db.session.commit()
    return user_schema.jsonify(user)


@app.route('/add', methods=['POST'])
def add_user():
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    jobtitle = request.json['jobtitle']
    phonenumber = request.json['phonenumber']
    country = request.json['country']

    user = User(firstname=firstname, lastname=lastname,
                jobtitle=jobtitle, phonenumber=phonenumber, country=country)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
