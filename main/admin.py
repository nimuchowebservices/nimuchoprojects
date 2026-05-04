from django.contrib import admin
from .models import Service, Project, ClientApplication, ContactMessage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client_name', 'completion_date')
    list_filter = ('category',)
    search_fields = ('title', 'client_name')

@admin.register(ClientApplication)
class ClientApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'service_type', 'status', 'submitted_date')
    list_filter = ('status', 'service_type')
    search_fields = ('full_name', 'email', 'phone')
    readonly_fields = ('submitted_date', 'updated_date')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_date', 'is_replied')
    list_filter = ('is_replied',)
    search_fields = ('name', 'email', 'subject')
