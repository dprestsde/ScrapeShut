from django.db import models

# Create your models here.

class UploadModel(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.IntegerField()
    photo = models.ImageField()
    file = models.FileField(blank=False, null=False)
    choice  = models.CharField(max_length=32)

    def __str__(self):
        return self.name