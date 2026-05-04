from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('apply/', views.apply_client, name='apply_client'),
    path('admin/applications/', views.client_applications, name='client_applications'),
    path('admin/update-status/<int:application_id>/', views.update_application_status, name='update_status'),
    path('admin/add-project/', views.add_project, name='add_project'),
    path('admin/contact-messages/', views.contact_messages, name='contact_messages'),
]
