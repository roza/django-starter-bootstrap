from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request, param):
    return HttpResponse("Hello Django ! "+param)

from lesTaches.models import Task

def task_listing(request):
    from django.template import Template, Context
    objects = Task.objects.all().order_by('due_date')
    template = Template('<ul>{% for elem in objects %}<li>{{elem}}{% endfor %}</ul>')
    print(str(template))
    context = Context({'objects': objects})
    print(str(template.render(context)))
    return HttpResponse(template.render(context))