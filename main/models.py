from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('graphic_design', 'Graphic Design'),
        ('web_development', 'Web Development'),
        ('digital_marketing', 'Digital Marketing'),
        ('branding', 'Branding'),
        ('video_editing', 'Video Editing'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_url = models.URLField(blank=True)
    completion_date = models.DateField()
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class ClientApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    SERVICE_CHOICES = [
        ('graphic_design', 'Graphic Design'),
        ('web_development', 'Web Development'),
        ('digital_marketing', 'Digital Marketing'),
        ('branding', 'Branding'),
        ('video_editing', 'Video Editing'),
        ('other', 'Other'),
    ]
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company_name = models.CharField(max_length=200, blank=True)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    project_description = models.TextField()
    budget_range = models.CharField(max_length=100, blank=True)
    timeline = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True)
    submitted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.full_name} - {self.service_type}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_date = models.DateTimeField(auto_now_add=True)
    is_replied = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name} - {self.subject}"
