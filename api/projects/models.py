from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    avatar = models.ImageField(upload_to="images/",null=True,blank=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name}"