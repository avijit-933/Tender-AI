from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import User






class Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    emp_id = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.emp_id

# app1/models.py


class Tender(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    tender_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    boq_file = models.FileField(upload_to='boq_files/')
    min_turnover = models.DecimalField(max_digits=15, decimal_places=2)
    min_experience = models.PositiveIntegerField(help_text="In years")
    certificates = models.CharField(max_length=200, blank=True, null=True)
    manpower = models.PositiveIntegerField(blank=True, null=True)
    weight_price = models.PositiveIntegerField(default=0)
    weight_experience = models.PositiveIntegerField(default=0)
    weight_technical = models.PositiveIntegerField(default=0)
    weight_performance = models.PositiveIntegerField(default=0)
    last_date = models.DateField()
    required_documents = models.CharField(max_length=200)
    category = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_weight(self):
        return self.weight_price + self.weight_experience + self.weight_technical + self.weight_performance

    def __str__(self):
        return f"{self.tender_id} - {self.title}"


