from django.db import models

# Create your models here.


class Tasks(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
