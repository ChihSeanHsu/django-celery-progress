from django.shortcuts import render
from django.http import JsonResponse

from tasks import my_task

# Create your views here.
def ajax_app(request):
    
    return render(request, 'app_ajax/index.html', {})

def get_ajax(request):
    print('ajax')
    result = my_task.delay(10)
    data = {
        'task_id': result.task_id
    }
    return JsonResponse(data)
