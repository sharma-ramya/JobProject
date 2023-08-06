from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.PointField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




