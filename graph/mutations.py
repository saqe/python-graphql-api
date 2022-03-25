import strawberry
from .type import LoginSuccess, LoginError, LoginResult, User

@strawberry.type
class Mutation:

    @strawberry.field
    def login(self, username: str, password: str) -> LoginResult:

        # Your domain-specific authentication logic would go here
        user = ...

        if user is None: return LoginError(message="Something went wrong")

        return LoginSuccess(user=User(name="My Name", age=234))