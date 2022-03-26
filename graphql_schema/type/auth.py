import strawberry
from . import User

class AuthType:
    @strawberry.type
    class LoginSuccess:
        access_token: str
        user: User

    @strawberry.type
    class LoginError:
        message: str