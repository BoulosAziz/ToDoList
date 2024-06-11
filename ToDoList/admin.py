from django.contrib import admin
from .models import Task

# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('task_name', 'deadline', 'username', 'is_done')
#     list_filter = ('username', 'is_done')
#     search_fields = ('task_name', 'description')

admin.site.register(Task)