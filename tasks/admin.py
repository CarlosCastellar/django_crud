from django.contrib import admin
from . import models

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
                       
# Register your models here.
admin.site.register(models.Task, TaskAdmin)