from django.db import models

class Institute(models.Model):
    name = models.CharField(max_length=100)
    no_of_courses = models.IntegerField()

    def __str__(self):
        return self.name
