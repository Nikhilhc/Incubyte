from django.db import models

# Create your models here.

class Words(models.Model):
    id = models.IntegerField(primary_key=True,blank=True,null=False)
    words = models.CharField(max_length=100)

    def __str__(self):
        return self.words