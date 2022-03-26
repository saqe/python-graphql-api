class FakeDatabase:
    def __init__(self):
        self.data = []

    def get(self, email: str):
        return {}

    def insert(self, user: dict):
        return {}