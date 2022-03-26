import strawberry

@strawberry.type
class Status:
    status: str
    message: str