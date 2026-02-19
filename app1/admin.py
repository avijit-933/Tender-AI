from django.contrib import admin

# Register your models here.
from django.contrib import admin
<<<<<<< HEAD
from .models import Officer
from .models import Bidder

admin.site.register(Officer)

from .models import Bidder

# admin.py


class BidderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'company_name', 
        'registration_number', 
        'gst_number', 
        'pan_number',
        'phone',
        'email',  # This is a property, not a database field
        'is_verified',  # Fixed: separated from password
        'created_at'
    ]
    list_filter = ['is_verified', 'created_at']
    search_fields = ['company_name', 'registration_number', 'gst_number', 'pan_number', 'user__email']
    readonly_fields = ['created_at']
    
    def email(self, obj):
        return obj.user.email
    email.short_description = 'Email Address'

admin.site.register(Bidder, BidderAdmin)

from .models import Officer,Tender


admin.site.register(Officer)
admin.site.register(Tender)

