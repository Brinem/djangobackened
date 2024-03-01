from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .form import TaskForm


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})


def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    return render(request, 'task_details.html', {'task': task})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            form = TaskForm()
        return render(request, 'task_form.html', {'form': form})


def task_edit(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail')
        else:
            form = TaskForm(instance=task)
            return render(request, 'task_form.html', {'form': form})


def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    else:
        task = TaskForm(instance=task)
        return render(request, 'task_form.html', {'task_confirmation': task})