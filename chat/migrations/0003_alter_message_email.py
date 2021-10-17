# Generated by Django 3.2.8 on 2021-10-14 13:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.CharField(max_length=24, validators=[django.core.validators.RegexValidator(regex='\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b/')]),
        ),
    ]