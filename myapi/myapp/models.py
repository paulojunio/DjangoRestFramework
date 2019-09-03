from django.db import models

# Create your models here.


class Pokemon(models.Model):

    class Meta:

        db_table = 'pokemon'

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    gen = models.IntegerField()

    def __str__(self):
        return self.name
