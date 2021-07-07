import graphene
# general schema
# import app schema
import todo.schema
import user.schema
import graphql_jwt


class Query(
    user.schema.Query,
    todo.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    user.schema.Mutation,
    todo.schema.Mutation,
    graphene.ObjectType
):
    # give us JWT token when logged
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify token_auth
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(mutation=Mutation)


schema = graphene.Schema(query=Query, mutation=Mutation)
