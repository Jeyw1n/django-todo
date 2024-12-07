from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'todo_list'

urlpatterns = [
    path('', views.ToDoListIndexView.as_view(), name='index'),
    path('done/', views.ToDoListDoneView.as_view(), name='done'),
    path('<int:pk>/', views.ToDoDetailView.as_view(), name='detail'),
    path('create/', views.ToDoItemCreateView.as_view(), name='create'),
]
