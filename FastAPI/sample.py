import uvicorn
from graphene import types as grt
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp


class Account(grt.ObjectType):
    account = grt.Int(required=True)


class AccountFilter(grt.InputObjectType):
    accounts = grt.List(grt.Int)


class Query(grt.ObjectType):
    course_list = None
    accounts = grt.Field(
        grt.List(Account),
        filters=AccountFilter(),
    )

    async def resolve_accounts(
        self,
        info,
        filters: AccountFilter,
    ):

        return [Account(account=1212), Account(account=43434)]


def get_graphql_app() -> GraphQLApp:
    return GraphQLApp(schema=grt.Schema(query=Query))


def init_app():
    app_ = Starlette()
    app_.mount("/graphql/", get_graphql_app())
    return app_


app = init_app()

if __name__ == "__main__":
    uvicorn.run(app=app)