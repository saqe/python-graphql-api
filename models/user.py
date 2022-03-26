from typing import Optional
from pydantic import BaseModel
from datetime import date

class UserModel(BaseModel):
    name: str
    email: str
    date_of_birth: Optional[date]
    hashed_password: str
    is_active: bool