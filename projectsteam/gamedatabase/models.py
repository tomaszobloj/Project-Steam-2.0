from django.db import models

class GameDatabase(models.Model):
    title = models.CharField(max_length=99)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
