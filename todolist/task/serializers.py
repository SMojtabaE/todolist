from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ("__all__")
        fields = ["title", "text", "is_done", "date_created"]

        
