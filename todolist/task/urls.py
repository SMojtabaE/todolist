from django.urls import path
from .views import SignUpCreateView,HomeTaskListView, TaskCreateview, TaskDetailview
            

app_name = 'task'

urlpatterns = [
    path('signup/',SignUpCreateView.as_view(),name='signup'),
    path('',HomeTaskListView.as_view(),name='home'),
    path('create_task/',TaskCreateview.as_view(),name='creat'),
    path('task_detail/<int:pk>',TaskDetailview.as_view(),name='detail_task'),
]
