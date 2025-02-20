# webapp/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to='covers/')
    metadata = models.TextField()
    reviews = models.TextField()
    publisher_info = models.TextField()

    def __str__(self):
        return self.title