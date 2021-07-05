from django.contrib import admin
from .models import clients
from .models import projects
# Register your models here.

admin.site.register(clients)
admin.site.register(projects)
