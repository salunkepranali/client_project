from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id'] 

class Client(models.Model):
    project_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='clents', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id'] 