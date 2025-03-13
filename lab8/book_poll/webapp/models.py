from django.db import models

class Vote(models.Model):
    CHOICES = [
        ('Good', 'Good'),
        ('Satisfactory', 'Satisfactory'),
        ('Bad', 'Bad'),
    ]
    choice = models.CharField(max_length=15, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
