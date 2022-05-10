# Generated by Django 4.0.4 on 2022-05-03 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0003_employee_lunch_finish_time_employee_lunch_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.PROTECT, related_name='employee', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]