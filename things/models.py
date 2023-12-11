from django.db import models
#in case not registered for second test
class Thing(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name