from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Databse configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flaskreact'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ma = Marshmallow(app)


@app.route('/')
def index():
    return jsonify({"hello": "Test version ssss"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
