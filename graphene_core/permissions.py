#!/usr/bin/env python
# coding=utf-8


class PermissionMixin(object):

    @classmethod
    def get_permissions(cls):
        return ()

    @classmethod
    def check_permission(cls, info):
        permissions = cls.get_permissions()
        if permissions:
            for permission in permissions:
                if permission().has_permission(info.context, info):
                    return True
            raise Exception("permission deny")
        return True
