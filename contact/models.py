from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    request = models.TextField()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
