from django.db import models


class English(models.Model):
    name = models.CharField(max_length=100, blank=True)
    title = models.TextField()
    def __str__(self):
        return self.name

class Ielts(models.Model):
    name = models.CharField(max_length=100, blank=True)
    title = models.TextField()
    def __str__(self):
        return self.name

