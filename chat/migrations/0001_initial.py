# Generated by Django 3.2.8 on 2021-10-14 11:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=24)),
                ('email', models.CharField(max_length=24, validators=[django.core.validators.RegexValidator(regex='/\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b/gm')])),
                ('text', models.TextField(validators=[django.core.validators.RegexValidator(regex='^.{,100}$'), django.core.validators.RegexValidator(regex='^(?!\\s*$).+')])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]