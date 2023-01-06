from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    patronymic = models.CharField(max_length=32)
    age = models.IntegerField()
    average_mark = models.FloatField()

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
