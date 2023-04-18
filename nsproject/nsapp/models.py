from django.db import models

class Client(models.Model):
    client_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('auth.User', related_name='clients', on_delete=models.CASCADE)

   
class Project(models.Model):
    project_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)

   