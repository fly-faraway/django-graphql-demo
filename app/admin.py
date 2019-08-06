from django.contrib import admin
from .models import Company, Department, Employee, Task


# Register your models here.
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Task)
