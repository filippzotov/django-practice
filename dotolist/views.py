from django.shortcuts import render
from django.http import HttpResponse
from .forms import TaskForm

# Create your views here.


def todolist(request):
    taskform = TaskForm()
    context = {
        "taskform": taskform,
    }
    return render(request, "todolist/todolist.html", context)
