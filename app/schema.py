#!/usr/bin/env python
# coding=utf-8


import graphene
from graphene import relay
from graphene_core.relay import PermissionObjectType, PermissionFilterConnectionField, Node
from rest_framework import permissions
from .models import Company, Department, Employee, Task
from .filters import CompanyFilterSet, DepartmentFilterSet, EmployeeFilterSet, TaskFilterSet


class CompanyNode(PermissionObjectType):

    @classmethod
    def get_permissions(cls):
        return permissions.IsAdminUser,

    class Meta:
        model = Company
        filterset_class = CompanyFilterSet
        interfaces = (relay.Node, )


class DepartmentNode(PermissionObjectType):

    class Meta:
        model = Department
        filterset_class = DepartmentFilterSet
        interfaces = (relay.Node, )


class EmployeeNode(PermissionObjectType):

    class Meta:
        model = Employee
        filterset_class = EmployeeFilterSet
        interfaces = (relay.Node, )


class TaskNode(PermissionObjectType):

    class Meta:
        model = Task
        filterset_class = TaskFilterSet
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    companies = PermissionFilterConnectionField(CompanyNode, description="公司列表")
    company = Node.Field(CompanyNode, description="公司")
    departments = PermissionFilterConnectionField(DepartmentNode, description="部门列表")
    department = Node.Field(DepartmentNode, description="部门")
    employees = PermissionFilterConnectionField(EmployeeNode, description="员工列表")
    employee = Node.Field(EmployeeNode, description="员工")
    tasks = PermissionFilterConnectionField(TaskNode, description="任务列表")
    task = Node.Field(TaskNode, description="任务")
