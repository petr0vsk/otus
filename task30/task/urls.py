from django.urls import path
from . import views 
from task.views import TaskListView, AboutTemplateView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('', TaskListView.as_view(), name = 'home'),
    path('about', AboutTemplateView.as_view(), name = 'about'),
    path('create', TaskCreateView.as_view(), name = 'create'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name = 'update'),
    path('task/<int:pk>', TaskDetailView.as_view(), name = 'task'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name = 'delete'),
]

