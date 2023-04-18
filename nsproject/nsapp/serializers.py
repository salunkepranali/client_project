from .models import Client, Project
from rest_framework import serializers


class ProjectSerilizer(serializers.ModelSerializer):
     
    class Meta:
        model = Project
        fields = '__all__'

class ClientSerilizer(serializers.ModelSerializer):
    Project = ProjectSerilizer(many=True,read_only=True)
    class Meta:
        model = Client
        fields = '__all__'



