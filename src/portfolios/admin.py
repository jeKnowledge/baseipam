from django.contrib import admin

# Register your models here.
from .models import Project, Event

admin.site.register(Project)
admin.site.register(Event)
