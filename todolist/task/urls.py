from django.urls import path
from .views import SignUpCreateView
            

app_name = 'task'

urlpatterns = [
    path('',SignUpCreateView.as_view(),name='signup'),
]
