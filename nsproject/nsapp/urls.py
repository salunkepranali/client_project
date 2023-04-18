from django.urls import path
from .views import ClientListView,ClientDetailView
from .views import ProjectListView

urlpatterns = [
    path('clients/', ClientListView.as_view()),
    path('api/clients/<int:pk>',ClientDetailView.as_view()),
    path('projects/',ProjectListView.as_view())
]