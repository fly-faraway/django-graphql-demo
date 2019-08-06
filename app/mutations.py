#!/usr/bin/env python
# coding=utf-8

from graphene_core.mutation import PermissionMutation
from .serializers import CompanySerializer, DepartmentSerializer, EmployeeSerializer, TaskSerializer


class CompanyMutation(PermissionMutation):

    class Meta:
        serializer_class = CompanySerializer


class DepartmentMutation(PermissionMutation):

    class Meta:
        serializer_class = DepartmentSerializer


class EmployeeMutation(PermissionMutation):

    class Meta:
        serializer_class = EmployeeSerializer


class TaskMutation(PermissionMutation):

    class Meta:
        serializer_class = TaskSerializer


class Mutation(object):
    company = CompanyMutation.Field(description="公司")
    department = CompanyMutation.Field(description="部门")
    employee = EmployeeMutation.Field(description="员工")
    task = TaskMutation.Field(description="任务")

