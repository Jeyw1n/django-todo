from django.http import (
    HttpRequest,
    HttpResponse
)
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)

from .models import ToDoItem
from .forms import ToDoItemForm


class ToDoListIndexView(TemplateView):
    template_name = 'todo_list/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_items'] = ToDoItem.objects.all()
        return context


# def index_view(request: HttpRequest) -> HttpResponse:
#     todo_items = TodoItem.objects.order_by('-id').all()

#     return render(
#         request, template_name='todo_list/index.html',
#         context={'todo_items': todo_items}
#     )

class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()


class ToDoDetailView(DetailView):
    model = ToDoItem


class ToDoItemCreateView(CreateView):
    model = ToDoItem
    # form_class = ToDoItemForm
    fields = ('title',)