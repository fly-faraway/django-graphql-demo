#!/usr/bin/env python
# coding=utf-8


from graphene_django import DjangoObjectType
import graphene
from graphene import relay, types
from graphene.types.utils import get_type
from functools import partial
from graphene import Connection
from graphene_django.filter import DjangoFilterConnectionField
from .permissions import PermissionMixin


class NodeField(types.Field):
    def __init__(self, node, type=False, deprecation_reason=None, name=None, description=None, **kwargs):
        assert issubclass(node, relay.Node), "NodeField can only operate in Nodes"
        self.node_type = node
        self.field_type = type

        super(NodeField, self).__init__(
            type or node,
            description=description,
            id=types.ID(required=True),
            )

    def get_resolver(self, parent_resolver):
        return partial(self.node_type.node_resolver, get_type(self.field_type))


class Node(relay.Node):

    @classmethod
    def Field(cls, *args, **kwargs):
        return NodeField(cls, *args, **kwargs)


class TotalCountConnection(Connection):
    total_count = graphene.Int()

    @staticmethod
    def resolve_total_count(root, info, **kwargs):
        return root.length

    class Meta:
        abstract = True


class PermissionObjectType(PermissionMixin, DjangoObjectType):
    @classmethod
    def __init_subclass_with_meta__(
            cls,
            model=None,
            registry=None,
            skip_registry=False,
            only_fields=(),
            fields=(),
            exclude_fields=(),
            exclude=(),
            filter_fields=None,
            filterset_class=None,
            connection=None,
            connection_class=None,
            use_connection=None,
            interfaces=(),
            convert_choices_to_enum=True,
            _meta=None,
            **options
    ):
        super(PermissionObjectType, cls).__init_subclass_with_meta__(
            model,
            registry,
            skip_registry,
            only_fields,
            fields,
            exclude_fields,
            exclude,
            filter_fields,
            filterset_class,
            connection,
            TotalCountConnection,
            use_connection,
            interfaces,
            convert_choices_to_enum,
            _meta,
            **options
        )

    @classmethod
    def get_node(cls, info, id):
        cls.check_permission(info)
        return super(PermissionObjectType, cls).get_node(info, id)

    class Meta:
        abstract = True


class PermissionFilterConnectionField(PermissionMixin, DjangoFilterConnectionField):

    @classmethod
    def connection_resolver(
            cls,
            resolver,
            connection,
            default_manager,
            max_limit,
            enforce_first_or_last,
            filterset_class,
            filtering_args,
            root,
            info,
            **args
    ):
        cls.check_permission(info)
        return super(PermissionFilterConnectionField, cls).connection_resolver(
            resolver,
            connection,
            default_manager,
            max_limit,
            enforce_first_or_last,
            filterset_class,
            filtering_args,
            root,
            info,
            total_count=10,
            **args
        )

