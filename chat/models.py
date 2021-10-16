from django.core.validators import RegexValidator
from django.db import models


class Message(models.Model):
    author = models.CharField(max_length=24)
    email = models.CharField(max_length=24, validators=[
        RegexValidator(
            # regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/'
            regex=r'[^@]+@[^@]+\.[^@]+'
        )
    ])

    text = models.TextField(validators=[
        RegexValidator(
            regex=r'^.{,100}$'
        ),
        RegexValidator(
            regex=r'^(?!\s*$).+'
        )
    ])
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
