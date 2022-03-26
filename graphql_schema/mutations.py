import strawberry
from .type import AuthType, Status
from models import UserModel
from database import FakeDatabase
from utils import Auth
from datetime import date

db = FakeDatabase()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def signup(self, email: str, password: str, name: str, date_of_birth: date) -> Status:
        # check if email is already in system.
        if db.is_exist(email): return Status(status="error", message= "Email already exists")

        # Convert password into hash.
        password = Auth.hash_plain_password(password)
        print(password)
        user = UserModel(
            name=name,
            email=email,
            hashed_password=password,
            date_of_birth=date_of_birth,
            is_active=False
        )

        db.insert(user)
        return Status(status="ok", message= "User registered, please signup now")

    @strawberry.mutation
    def login(self, username: str, password: str) -> AuthType.LoginSuccess:
        raise AttributeError("Can't find user")

        return AuthType.LoginSuccess(user=User(name="My Name", age=234))