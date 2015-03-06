from app import db
from app.main.models import User

import factory
from factory.alchemy import SQLAlchemyModelFactory

class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    email = factory.Sequence(lambda n: "user_{}@example.com".format(n))
    password = "password"
