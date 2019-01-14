from django.shortcuts import render
from tasks import my_task

# Create your views here.
def normal_app(request):
    result = my_task.delay(10)
    return render(request, 'app_normal/index.html', context={'task_id': result.task_id})
