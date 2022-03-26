import strawberry
from . import User

class AuthType:
    @strawberry.type
    class LoginSuccess:
        user: User

    @strawberry.type
    class LoginError:
        message: str