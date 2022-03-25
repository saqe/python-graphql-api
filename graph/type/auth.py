import strawberry
from . import User

@strawberry.type
class LoginSuccess:
    user: User

@strawberry.type
class LoginError:
    message: str


LoginResult = strawberry.union("LoginResult", (LoginSuccess, LoginError))
