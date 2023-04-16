from rest_framework import serializers
from .models import Project
from .models import Client
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Project
        fields = ('id', 'name', 'creator','created_at')

class ClientSerializer(serializers.ModelSerializer):  # create class to serializer model

    class Meta:
        model = Client
        fields = ('id', 'name', 'creator','created_at','created_by')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    clients = serializers.PrimaryKeyRelatedField(many=True, queryset=Client.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'created_at','created_by')
