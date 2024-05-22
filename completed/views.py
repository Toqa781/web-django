from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from tasks.models import Task

# View to display the main page with completed tasks
def mainpage(request):
    tasks = Task.objects.filter(completed=True)
    return render(request, 'mainpage.html', {'tasks': tasks})

# View to display the details of a specific task
def task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)  # Filter by primary key (pk)
    return render(request, 'ctask.html', {'task': task})

# View to mark a task as not done
@require_POST
@csrf_exempt  # Only use csrf_exempt for demonstration purposes; in production, ensure CSRF is handled properly
def mark_as_done(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not (task.competed)
    task.save()
    return JsonResponse({'status': 'success', 'completed': task.completed})
