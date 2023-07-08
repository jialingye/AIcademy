from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DataTimeField(auto_now_add=True)

    def __Str__(self):
        return self.title
