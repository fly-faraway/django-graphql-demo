#!/usr/bin/env python
# coding=utf-8

from graphene_core.serializers import BaseSerializer
from .models import Company, Department, Employee, Task


class CompanySerializer(BaseSerializer):

    class Meta:
        model = Company
        fields = "__all__"


class DepartmentSerializer(BaseSerializer):

    class Meta:
        model = Department
        fields = "__all__"


class EmployeeSerializer(BaseSerializer):

    class Meta:
        model = Employee
        fields = "__all__"


class TaskSerializer(BaseSerializer):

    class Meta:
        model = Task
        fields = "__all__"
