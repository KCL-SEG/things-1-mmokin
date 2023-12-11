from django.db import models
#in case not registered for second test
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(default=0, blank=False, choices=[(i, i) for i in range(101)])

    def __str__(self):
        return self.name
