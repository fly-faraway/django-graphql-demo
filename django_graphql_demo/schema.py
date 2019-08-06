#!/usr/bin/env python
# coding=utf-8


import graphene
import graphql_jwt
from app.schema import Query as AppQuery
from app.mutations import Mutation as AppMutation


class Query(AppQuery, graphene.ObjectType):
    pass


class Mutation(AppMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
