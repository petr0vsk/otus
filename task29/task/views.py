from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView 


class TaskListView(ListView):
    model = Task
    template_name = 'task/index.html'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task/create.html'
    success_url = '/'
    form_class = TaskForm


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/create.html'
    success_url = '/'
    form_class = TaskForm


class AboutTemplateView(TemplateView):
    template_name = 'task/about.html'

class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'
    # страница для подтверждения удаления
    template_name = 'task/delete_confirm.html'    


