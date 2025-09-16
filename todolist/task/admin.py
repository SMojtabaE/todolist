from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ("title","user","is_done","date_created")
    list_filter = ("date_created","user","is_done")

admin.site.register(Task, TaskAdmin)