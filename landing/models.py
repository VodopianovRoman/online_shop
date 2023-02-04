from django.db import models

# Create your models here.


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.id}; {self.email}; {self.name}'

    def __repr__(self):
        return f"{Subscriber.__name__}(id={self.id})"