from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListCreateProjectAPIView.as_view(), name='get_post_projects'),
    path('<int:pk>/', views.RetrieveUpdateDestroyProjectAPIView.as_view(), name='get_delete_update_project'),
     path('', views.ListCreateClientAPIView.as_view(), name='get_post_clients'),
    path('<int:pk>/', views.RetrieveUpdateDestroyClientAPIView.as_view(), name='get_delete_update_client'),
]