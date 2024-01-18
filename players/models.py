from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200)
    hand = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    birthdate = models.DateField()

    class Meta:
        ordering = ('birthdate',)
        indexes = [
            models.Index(fields=['name',]),
            models.Index(fields=['country',]),
            models.Index(fields=['birthdate',]),
        ]

    def __str__(self):
        return self.name
    
