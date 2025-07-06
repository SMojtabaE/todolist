from django.urls import path
from .views import (SignUpCreateView,HomeTaskListView,TaskCreateview,
                        TaskDetailview, TaskUpdateView, TaskDeleteView)
            

app_name = 'task'

urlpatterns = [
    path('signup/',SignUpCreateView.as_view(),name='signup'),
    path('',HomeTaskListView.as_view(),name='home'),
    path('create_task/',TaskCreateview.as_view(),name='create_task'),
    path('detail_task/<int:pk>',TaskDetailview.as_view(),name='detail_task'),
    path('update_task/<int:pk>',TaskUpdateView.as_view(),name='update_task'),
    path('delete_task/<int:pk>',TaskDeleteView.as_view(),name='delete_task'),
]
