from django.db import models

# Create your models here.
class Author:
    def __init__(self, name, birthday_year):
        self.name = name
        self.birthday_year = birthday_year

    def __str__(self):
        return f'{self.name}'


class Biography:
    def __init__(self, text, author):
        self.text = text
        self.author = author
