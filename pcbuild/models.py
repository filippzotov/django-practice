from django.db import models

# Create your models here.
class TypeItem(models.Model):

    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class PCpiece(models.Model):

    name = models.CharField(max_length=200)
    typeitem = models.ForeignKey("TypeItem", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
