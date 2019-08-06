#!/usr/bin/env python
# coding=utf-8

from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    id = serializers.CharField()


