# Generated by Django 2.2.3 on 2019-08-02 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='公司名', max_length=256, verbose_name='公司名')),
                ('website', models.URLField(help_text='网址', verbose_name='网址')),
            ],
            options={
                'verbose_name': '公司',
                'verbose_name_plural': '公司',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='部门名称', max_length=256, verbose_name='部门名称')),
                ('company', models.ForeignKey(help_text='所属公司', on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='app.Company', verbose_name='所属公司')),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='姓名', max_length=256, verbose_name='姓名')),
                ('email', models.EmailField(default=None, help_text='邮箱', max_length=254, verbose_name='邮箱')),
                ('department', models.ForeignKey(help_text='所属部门', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='app.Department', verbose_name='所属部门')),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='任务名', max_length=256, verbose_name='任务名')),
                ('deadline', models.DateField(help_text='截止日期', verbose_name='截止日期')),
                ('is_finished', models.BooleanField(default=False, help_text='是否已完成', verbose_name='是否已完成')),
                ('members', models.ManyToManyField(help_text='成员', to='app.Employee', verbose_name='成员')),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
            },
        ),
    ]
