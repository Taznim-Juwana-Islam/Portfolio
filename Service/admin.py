from django.contrib import admin
from Service.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("website_title", "website_description", "date", "status", "image")


admin.site.register(Service, ServiceAdmin)
