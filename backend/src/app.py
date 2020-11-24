from flask import Flask, jsonify, request
from flask_cors import CORS

from .entities.entity import Base, engine, Session
from .entities.user import User, UserSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed generate database schema
Base.metadata.create_all(engine)


@app.route('/')
def home():
    return "divide et impera"


@app.route('/users')
def get_users():
    # fetch db
    session = Session()
    users = session.query(User).all()

    schema = UserSchema(many=True)
    jusers = schema.dump(users)

    session.close()
    return jsonify(jusers)


@app.route('/users', methods=['POST'])
def add_user():
    new_user = UserSchema().load(request.get_json())
    user = User(**new_user)

    session = Session()
    session.add(user)
    session.commit()

    result = False
    if len(UserSchema().dump(user)) > 0:
        result = True
    session.close()
    return str(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
