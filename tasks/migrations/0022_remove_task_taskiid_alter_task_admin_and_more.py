# Generated by Django 5.0.6 on 2024-05-23 19:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0021_task_admins_alter_task_admin'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Taskiid',
        ),
        migrations.AlterField(
            model_name='task',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='admins',
            field=models.ManyToManyField(related_name='admin_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
