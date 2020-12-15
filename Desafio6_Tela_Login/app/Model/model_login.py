import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


BaseAlchemy = declarative_base()


class AdministratorModel(BaseAlchemy):
    __tablename__ = 'ADMINISTRATOR'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=50))
    password = db.Column(db.String(length=50))
    email = db.Column(db.String(length=100))
    active = db.Column(db.Boolean, default=True)

    def __init__(self, active=True, id=None):
        self.id = id
        self.username = input("Informe o username: ")
        self.password = input("Informe o password: ")
        self.email = input("Informe o email: ")
        self.active = active

    def __str__(self):
        return f"ID user: {self.id}\n" \
               f"Username: {self.username}\n" \
               f"Password: {self.password}\n" \
               f"Email: {self.email}\n" \
               f"Active: {self.active}\n"
