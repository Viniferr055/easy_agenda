# Generated by Django 4.0.4 on 2022-04-30 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]