from graphql_schema.type import User

class FakeDatabase:
    def __init__(self):
        self.__data = []

    def get(self, email: str) -> User:
        return next(self.__query(email))

    def insert(self, user: User):
        self.__data.append(user)
        return user

    def list(self):
        return self.__data

    def is_exist(self, email: str):
        return any(self.__query(email))

    def __query(self, email: str):
        return filter(lambda user: user.email== email, self.__data)