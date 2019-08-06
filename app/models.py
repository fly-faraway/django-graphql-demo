from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=256, verbose_name="公司名", help_text="公司名")
    website = models.URLField(verbose_name="网址", help_text="网址")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "公司"
        verbose_name_plural = "公司"


class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="departments",
                                verbose_name="所属公司", help_text="所属公司")
    name = models.CharField(max_length=256, verbose_name="部门名称", help_text="部门名称")

    def __str__(self):
        return "%s%s" % (self.company.name, self.name)

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门"


class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True,
                                   related_name="employees", verbose_name="所属部门", help_text="所属部门")
    name = models.CharField(max_length=256, verbose_name="姓名", help_text="姓名")
    email = models.EmailField(default=None, verbose_name="邮箱", help_text="邮箱")

    def __str__(self):
        return "%s%s" % (self.department.__str__(), self.name)

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = "员工"


class Task(models.Model):
    name = models.CharField(max_length=256, verbose_name="任务名", help_text="任务名")
    members = models.ManyToManyField(Employee, verbose_name="成员", help_text="成员")
    deadline = models.DateField(verbose_name="截止日期", help_text="截止日期")
    is_finished = models.BooleanField(default=False, verbose_name="是否已完成", help_text="是否已完成")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "任务"
        verbose_name_plural = "任务"
