from django.contrib import admin
from todo_list.models import ToDoItem

@admin.register(ToDoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'done'
    list_display_links = 'id', 'title'