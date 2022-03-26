from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext
from os import getenv

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
    def get_access_token(user):
        to_encode = {'user_id': user.id}
        expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def verify_jwt_access_token(token):
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])