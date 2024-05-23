from django.shortcuts import render
from .models import Task
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task
from myapp.models import User
@login_required
def showTask(request):
    try:
        # Fetch tasks associated with the currently logged-in admin user
        tasks = Task.objects.filter(admin=request.user)
    except Exception as e:
        tasks = None
        print('Exception:', e)
        # You may want to log the error or display a more user-friendly message

    context = {
        'task': tasks,  # Pass tasks to the template context
    }
    
    return render(request, 'AdminHome/AdminHome.html', context)

    
def task_detail(request,taskid):
    return render(request, 'task.html', {'Task': get_object_or_404(Task,id=taskid )})

def viewlist(request):
    return render(request, 'viewlist.html')


def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('showTask')
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

