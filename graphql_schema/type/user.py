from datetime import date
import strawberry
from typing import Optional

@strawberry.type
class User:
    name: str
    email: str
    date_of_birth: Optional[date]

    # Virtually resolved field.
    @strawberry.field
    def greet(self) -> str:
        return f"Hi {self.name}!"

    # Virtual Field
    current_date: date = strawberry.field(resolver=lambda: date.today())