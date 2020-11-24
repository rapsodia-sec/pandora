from sqlalchemy import Column, String
from .entity import Entity, Base
from marshmallow import Schema, fields


class User(Entity, Base):
    __tablename__ = 'users'

    username = Column(String)
    fname = Column(String)
    lname = Column(String)
    email = Column(String)
    passwordhash = Column(String)

    def __init__(self, username, fname, lname, email, passwordhash):
        Entity.__init__(self, fname + " " + lname)
        self.username = username
        self.fname = fname
        self.lname = lname
        self.email = email
        self.passwordhash = passwordhash

class UserSchema(Schema):
    id = fields.Integer()
    username = fields.Str()
    fname = fields.Str()
    lname = fields.Str()
    email = fields.Str()
    passwordhash = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()