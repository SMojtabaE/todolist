from django.urls import path
from .views import (    
                        SignUpCreateView,TaskListView,TaskCreateview,
                        TaskDetailview, TaskUpdateView, TaskDeleteView,
                        HomeView

                    )
            

app_name = 'task'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('signup/',SignUpCreateView.as_view(),name='signup'),
    path('list_task',TaskListView.as_view(),name='list_task'),
    path('create_task/',TaskCreateview.as_view(),name='create_task'),
    path('detail_task/<int:pk>',TaskDetailview.as_view(),name='detail_task'),
    path('update_task/<int:pk>',TaskUpdateView.as_view(),name='update_task'),
    path('delete_task/<int:pk>',TaskDeleteView.as_view(),name='delete_task'),
]
