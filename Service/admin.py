from django.contrib import admin
from Service.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("Project_title", "Project_description", "dates", "Project_status", "image")


admin.site.register(Service, ServiceAdmin)
