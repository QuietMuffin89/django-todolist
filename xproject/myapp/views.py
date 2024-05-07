from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def index(request):

    todos = Todo.objects.all()

    return render(
        request=request,
        template_name="myapp/index.html",
        context={
        #    "item_qs": item_qs
        "todos" : todos
        }
    )

def add_todo(request):
    if request.method == "POST":
        todo = Todo(content=request.POST.get("content"),
             completed=False
             )
        todo.save()

    return redirect(index)

def delete_todo(request, todo_id):
    if request.method == "POST":
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()

    return redirect(index)