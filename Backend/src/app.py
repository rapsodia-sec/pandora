from flask import Flask, jsonify, request
from .entities.entity import Base, engine, Session
from .entities.user import User, UserSchema

# creating the Flask application
app = Flask(__name__)

# if needed generate database schema
Base.metadata.create_all(engine)



# if len(users) == 0:
#     # create and persist mock user
#     new_user = User("rapsodia", "Mattia", "Dall'Antonia", "mattiadallantonia@rapsodia-sec.com", "$2y$12$5R3108L7GQQpM7M3EfdCvuzD0f4IympCXnH.2ksg70R8fQ/ulMZYO")
#     session.add(new_user)
#     session.commit()
#     session.close()
#
#     # reload users
#     users = session.query(User).all()




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
