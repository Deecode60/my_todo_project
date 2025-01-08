from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/<uuid:id>/', views.todo_detail, name='todo_detail'),
]
