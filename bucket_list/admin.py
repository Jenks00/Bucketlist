from django.contrib import admin
from .models import To_do


@admin.register(To_do)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('Task', 'user', 'complete', 'created', 'completed')
    list_filter = ('complete',)
    search_fields = ('Task',)
