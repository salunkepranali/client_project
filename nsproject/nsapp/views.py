from rest_framework import generics
from .serializers import ClientSerilizer, ProjectSerilizer
from .models import Client, Project
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
# Create your views here.

class ClientListView(generics.ListCreateAPIView):
    serializer_class = ClientSerilizer
    queryset = Client.objects.all()
   

class ProjectListView(generics.ListCreateAPIView):
    serializer_class = ProjectSerilizer
    queryset = Project.objects.all()
    

class ClientListView(APIView):
    def get(self,request):
        clients = Client.objects.all()
        serializer = ClientSerilizer(clients,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        clientserializer = ClientSerilizer(data=request.data)
        if clientserializer.is_valid():
            clientserializer.save()
            return Response(clientserializer.data,status=status.HTTP_201_CREATED)
        return Response(clientserializer.errors)
    
class ClientDetailView(APIView):
    def get_client(self,pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        client = self.get_client(pk)
        serializer = ClientSerilizer(client)
        return Response(serializer.data)


    def delete(self,request,pk):
        self.get_client(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self,request,pk):
        client = self.get_client(pk)
        clientSerializer = ClientSerilizer(client,data = request.data)
        if clientSerializer.is_valid():
            clientSerializer.save()
            return Response(clientSerializer.data)
        return Response(clientSerializer.errors)