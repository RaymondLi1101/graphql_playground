import graphene, graphql_jwt

import links.schema
import links.schema_relay
import hackernews.users.schema


class Query(hackernews.users.schema.Query, links.schema.Query, links.schema_relay.RelayQuery, graphene.ObjectType):
    pass


class Mutation(links.schema.Mutation, hackernews.users.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

