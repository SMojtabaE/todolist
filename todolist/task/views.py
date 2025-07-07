from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
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
    paginate_by = 10
    context_object_name = 'task_list'
    def get_queryset(self):

        queryset = Task.objects.filter(user=self.request.user)  # Start with the default queryset
        status_filter = self.request.GET.get('status')
        print(status_filter)
        # /?status=completed
        # ?status=pending
        if status_filter:
            if status_filter=='completed':
                queryset = queryset.filter(user=self.request.user, is_done=True)
            elif status_filter=='pending':
                queryset = queryset.filter(user=self.request.user, is_done=False)


        return queryset


class TaskDetailview(LoginRequiredMixin,DetailView):           # tempalte = > task_detail.html
    model = Task


class TaskUpdateView(LoginRequiredMixin,UpdateView):          
    model = Task
    template_name = 'task/task_update.html'
    fields = ['title', 'text','is_done']
    success_url = reverse_lazy('task:home')

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy('task:home')