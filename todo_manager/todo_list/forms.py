from django import forms

from .models import ToDoItem

# Не используется
class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('title',)

        # widgets = {
        #     'title': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
        # }