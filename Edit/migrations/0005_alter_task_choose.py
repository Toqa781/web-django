# Generated by Django 5.0.6 on 2024-05-23 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Edit', '0004_remove_task_id_alter_task_taskiid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='choose',
            field=models.CharField(choices=[('Low', 'Low'), ('High', 'High'), ('Medium', 'Medium')], max_length=7, null=True),
        ),
    ]