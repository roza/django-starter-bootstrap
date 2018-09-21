from django.contrib import admin

# Register your models here.
from lesTaches.models import Task



class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_date', 'colored_due_date')

admin.site.register(Task, TaskAdmin)