# Generated by Django 5.0.6 on 2024-05-15 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_alter_task_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='choose',
            field=models.CharField(choices=[('Low', 'Low'), ('High', 'High'), ('Medium', 'Medium')], default='Low', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='teacher',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
