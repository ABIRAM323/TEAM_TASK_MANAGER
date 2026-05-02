from django.urls import path
from .views import task_list, task_create, update_task_status

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('<int:pk>/status/', update_task_status, name='update_task_status'),
]
