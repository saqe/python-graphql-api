from fastapi import FastAPI
from strawberry.asgi import GraphQL
from strawberry import Schema
from graphql_schema import Query, Mutation
from starlette.responses import RedirectResponse

schema = Schema(query=Query, mutation=Mutation)

graphql_app = GraphQL(schema)

app = FastAPI()

# Redirect Get root request to graphql endpoint
@app.get("/")
async def redirect():
    return RedirectResponse(url='/graphql')

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)