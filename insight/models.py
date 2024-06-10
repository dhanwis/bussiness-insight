from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=20)
    subject=models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    # phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
      return f'{self.name} - {self.email}'
  