from django.contrib import admin
from .models import Project_manager
class Project_manager_admin(admin.ModelAdmin):

    list_display = ('name','project')
admin.site.register(Project_manager,Project_manager_admin)
