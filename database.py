from models import UserModel

class FakeDatabase:
    def __init__(self):
        self.__data = []

    def get(self, email: str) -> UserModel:
        return next(self.__query(email))

    def insert(self, user: UserModel):
        self.__data.append(user)
        return user

    def list(self):
        return self.__data

    def is_exist(self, email: str):
        return any(self.__query(email))

    def __query(self, email: str):
        return filter(lambda user: user.email== email, self.__data)