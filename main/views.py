from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from .models import Service, Project, ClientApplication, ContactMessage
from .forms import ClientApplicationForm, ContactForm
from django.core.paginator import Paginator
from django.db.models import Q

def is_admin(user):
    return user.is_superuser or user.is_staff

def home(request):
    services = Service.objects.all()[:6]
    recent_projects = Project.objects.all().order_by('-completion_date')[:3]
    return render(request, 'main/home.html', {
        'services': services,
        'recent_projects': recent_projects,
    })

def about(request):
    return render(request, 'main/about.html')

def services(request):
    all_services = Service.objects.all()
    return render(request, 'main/services.html', {'services': all_services})

def projects(request):
    category = request.GET.get('category', '')
    if category:
        project_list = Project.objects.filter(category=category)
    else:
        project_list = Project.objects.all().order_by('-completion_date')
    
    paginator = Paginator(project_list, 6)
    page_number = request.GET.get('page')
    projects_page = paginator.get_page(page_number)
    
    return render(request, 'main/projects.html', {
        'projects': projects_page,
        'current_category': category,
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

def apply_client(request):
    if request.method == 'POST':
        form = ClientApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, 'Your application has been submitted successfully! We will review it and contact you soon.')
            return redirect('home')
    else:
        form = ClientApplicationForm()
    
    return render(request, 'main/client_application.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def client_applications(request):
    status_filter = request.GET.get('status', '')
    search_query = request.GET.get('search', '')
    
    applications = ClientApplication.objects.all().order_by('-submitted_date')
    
    if status_filter:
        applications = applications.filter(status=status_filter)
    
    if search_query:
        applications = applications.filter(
            Q(full_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone__icontains=search_query)
        )
    
    paginator = Paginator(applications, 10)
    page_number = request.GET.get('page')
    applications_page = paginator.get_page(page_number)
    
    stats = {
        'total': ClientApplication.objects.count(),
        'pending': ClientApplication.objects.filter(status='pending').count(),
        'approved': ClientApplication.objects.filter(status='approved').count(),
        'rejected': ClientApplication.objects.filter(status='rejected').count(),
    }
    
    return render(request, 'main/client_applications.html', {
        'applications': applications_page,
        'stats': stats,
        'status_filter': status_filter,
        'search_query': search_query,
    })

@login_required
@user_passes_test(is_admin)
def update_application_status(request, application_id):
    application = get_object_or_404(ClientApplication, id=application_id)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        admin_notes = request.POST.get('admin_notes', '')
        
        application.status = new_status
        application.admin_notes = admin_notes
        application.save()
        
        messages.success(request, f'Application status updated to {new_status}')
        return redirect('client_applications')
    
    return render(request, 'main/update_status.html', {'application': application})

@login_required
@user_passes_test(is_admin)
def add_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        client_name = request.POST.get('client_name')
        completion_date = request.POST.get('completion_date')
        project_url = request.POST.get('project_url', '')
        
        project = Project.objects.create(
            title=title,
            category=category,
            description=description,
            client_name=client_name,
            completion_date=completion_date,
            project_url=project_url
        )
        
        if request.FILES.get('image'):
            project.image = request.FILES['image']
            project.save()
        
        messages.success(request, 'Project added successfully!')
        return redirect('projects')
    
    return render(request, 'main/add_project.html')

@login_required
@user_passes_test(is_admin)
def contact_messages(request):
    messages_list = ContactMessage.objects.all().order_by('-submitted_date')
    return render(request, 'main/contact_messages.html', {'messages': messages_list})


from django.http import HttpResponse
from django.contrib.auth.models import User
import os

def create_superuser_temp(request):
    secret = request.GET.get('secret')
    if secret != 'nimucho2026':
        return HttpResponse("Access denied", status=403)
    username = os.environ.get('SU_USER', 'admin')
    email = os.environ.get('SU_EMAIL', 'admin@example.com')
    password = os.environ.get('SU_PASSWORD', 'Nimucho2026!')
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse(f"Superuser '{username}' created successfully!")
    else:
        return HttpResponse(f"Superuser '{username}' already exists.")


from django.http import HttpResponse
from django.contrib.auth.models import User
def reset_admin_password(request):
    secret = request.GET.get('secret')
    if secret != 'nimucho2026':
        return HttpResponse("Access denied", status=403)
    try:
        user = User.objects.get(username='admin')
        user.set_password('Nimucho2026!')
        user.save()
        return HttpResponse("Password for 'admin' has been reset to 'Nimucho2026!'")
    except User.DoesNotExist:
        return HttpResponse("User 'admin' does not exist", status=404)
