# Generated by Django 5.0.6 on 2024-05-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_rename_id_task_taskid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='Taskid',
            new_name='TaskId',
        ),
    ]