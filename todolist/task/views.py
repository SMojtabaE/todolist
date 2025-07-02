from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin 
        
# Create your views here.

class SignUpCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    template_name = 'registration/signup.html'


class TaskCreateview(LoginRequiredMixin,CreateView):           # templat = > task_form.html
    model = Task
    fields = ['title','text']

    success_url = reverse_lazy('task:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class HomeTaskListView(LoginRequiredMixin,ListView):   #home page           # template = > index.html
    model = Task
    template_name = 'task/index.html'

    context_object_name = 'task_list'
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskDetailview(LoginRequiredMixin,DetailView):           # tempalte = > task_detail.html
    model = Task