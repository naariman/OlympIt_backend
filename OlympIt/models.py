from django.db import models


class Lesson(models.Model):
    TYPE_CHOICES = (
        ('exam', 'ЕГЭ'),
        ('olymp', 'Олимпиада')
    )

    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    icon_url = models.URLField()
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name