#!/usr/bin/env python
# coding=utf-8


from django.shortcuts import get_object_or_404
from graphql_relay import from_global_id
from graphene_django.rest_framework.mutation import SerializerMutation
from .permissions import PermissionMixin


class PermissionMutation(PermissionMixin, SerializerMutation):

    @classmethod
    def get_serializer_kwargs(cls, root, info, **input):
        lookup_field = cls._meta.lookup_field
        model_class = cls._meta.model_class

        if model_class:
            if "update" in cls._meta.model_operations and lookup_field in input:
                pk = from_global_id(input.pop(lookup_field))[1]
                instance = get_object_or_404(
                    model_class, **{lookup_field: pk}
                )
                partial = True
            elif "create" in cls._meta.model_operations:
                instance = None
                partial = False
            else:
                raise Exception(
                    'Invalid update operation. Input parameter "{}" required.'.format(
                        lookup_field
                    )
                )

            return {
                "instance": instance,
                "data": input,
                "context": {"request": info.context},
                "partial": partial,
            }

        return {"data": input, "context": {"request": info.context}}

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        cls.check_permission(info)
        return super(PermissionMutation, cls).mutate_and_get_payload(root, info, **input)

    class Meta:
        abstract = True
