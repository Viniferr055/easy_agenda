# Generated by Django 4.0.4 on 2022-06-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_employee_complement_alter_employee_crm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='end_time',
            field=models.TimeField(blank=True, default='18:00:00', null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='start_time',
            field=models.TimeField(blank=True, default='08:00:00', null=True),
        ),
    ]
