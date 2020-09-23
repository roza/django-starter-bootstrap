from lesTaches.models import Task
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(request, param):
    return HttpResponse("Hello Django ! "+param)


def task_listing(request):
    objects = Task.objects.all().order_by('due_date')

    return render(request, template_name='list2.html', context={'objects': objects})
