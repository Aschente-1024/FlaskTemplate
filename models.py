from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

    def as_dict(self):
        return {user.name: getattr(self, user.name) for user in self.__table__.columns}

    def __repr__(self):
        return f'({self.__tablename__}: {self.name})\n'
