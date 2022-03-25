import strawberry
from typing import Optional

@strawberry.type
class User:
    name: str
    age: Optional[int]