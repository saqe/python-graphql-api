import strawberry
from .type import AuthType, User, Status

@strawberry.type
class Mutation:
    @strawberry.mutation
    def signup(self, email: str, password: str, username: str) -> Status:
        return Status(status="ok", message= "logged in")

    @strawberry.mutation
    def login(self, username: str, password: str) -> AuthType.LoginSuccess:

        # Your domain-specific authentication logic would go here
        user = ...
        return AuthType.LoginSuccess(user=User(name="My Name", age=234))