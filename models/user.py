from sqlalchemy import Boolean, Column, Integer, String, DateTime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable= False)
    is_active = Column(Boolean, nullable= False, default=True)
    inserted_at = Column(DateTime, nullable= False, default=DateTime.utcnow)
    last_logged_at = Column(DateTime)