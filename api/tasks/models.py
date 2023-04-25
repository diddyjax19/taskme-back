from django.db import models
from api.projects.models import Project
from api.users.models import CustomUser

# Create your models here.
class Task(models.Model):
    STATUS = (
        ('NEW','NEW'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('CLOSED','CLOSED'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length = 250)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assignedTo = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subtasks = models.ManyToManyField('Task', related_name="sub_tasks",blank=True,null=True)
    state = models.CharField(max_length=11,choices=STATUS,default="NEW")

    def __str__(self):
        return str(self.name)

