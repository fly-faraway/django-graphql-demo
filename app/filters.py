#!/usr/bin/env python
# coding=utf-8

import django_filters
from .models import Company, Department, Employee, Task


class CompanyFilterSet(django_filters.FilterSet):

    class Meta:
        model = Company
        fields = {
            "name": ["icontains"],
        }


class DepartmentFilterSet(django_filters.FilterSet):
    class Meta:
        model = Department
        fields = {
            "company": ["exact"],
        }


class EmployeeFilterSet(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = {
            "department": ["exact"],
            "department__company": ["exact"],
        }


class TaskFilterSet(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = {
            "name": ["icontains"],
        }
