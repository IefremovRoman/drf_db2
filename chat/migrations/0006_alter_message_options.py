# Generated by Django 3.2.8 on 2021-10-15 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_message_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['id']},
        ),
    ]
