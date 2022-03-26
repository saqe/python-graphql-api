from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext
from os import getenv
from models import UserModel

SECRET_KEY = getenv('SECRET_KEY')
ALGORITHM = "HS256"

class Auth:
    __pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash_plain_password(password) -> str:
        return Auth.__pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password) -> str:
        return Auth.__pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def authenticate_user(email: str, password: str):
        # get user
        user= ...
        # get password hash
        # verify password hash
        # verify if user is active
        # return user
        # else return Exception message of user not found
        pass

    @staticmethod
    def get_access_token(user: UserModel):
        payload = {
            'name': user.name,
            'active': user.is_active,
            'exp': datetime.utcnow() + timedelta(minutes=15)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    @staticmethod
    def verify_jwt_access_token(token):
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])