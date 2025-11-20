from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


@login_required
def todo_home(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            Todo.objects.create(user=request.user, task=task)
        return redirect("todo-home")

    todos = Todo.objects.filter(user=request.user)
    return render(request, "todo_home.html", {"todos": todos})

@login_required
def update_task(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)

    if request.method == "POST":
        updated_task = request.POST.get("task")
        todo.task = updated_task
        todo.save()
        return redirect("todo-home")

    return render(request, "update_task.html", {"todo": todo})

@login_required
def delete_task(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect("todo-home")

def logout_page(request):
    return render(request, "logout.html")

