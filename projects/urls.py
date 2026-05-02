from django.urls import path
from .views import project_list, project_create, project_detail, add_member

urlpatterns = [
    path('', project_list, name='project_list'),
    path('create/', project_create, name='project_create'),
    path('<int:pk>/', project_detail, name='project_detail'),
    path('<int:pk>/add-member/', add_member, name='add_member'),
]
