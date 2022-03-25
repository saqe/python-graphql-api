import strawberry
from .type import User
from typing import List

@strawberry.type
class Query:
    @strawberry.field
    def get_user(self) -> User:
        return User(name="Patrick")

    @strawberry.field
    def users(self) -> List[User]:
        return [User(name="Patrick", age=100)]
