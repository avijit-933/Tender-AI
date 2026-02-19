from django.contrib import admin
from .models import Officer, Bidder, Tender


@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    # Use fields that exist in your Officer model
    list_display = ['id', 'name', 'email', 'phone']  # Adjust based on your actual fields
    search_fields = ['name', 'email']
    
    # If you have these fields, add them:
    # list_filter = ['department', 'designation']

@admin.register(Bidder)
class BidderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 
        'company_name', 
        'registration_number', 
        'gst_number', 
        'pan_number',
        'phone',
        'get_email',
        'is_verified',
        'created_at'
    ]
    list_filter = ['is_verified', 'created_at']
    search_fields = ['company_name', 'registration_number', 'gst_number', 'pan_number', 'user__email']
    readonly_fields = ['created_at']
    
    def get_email(self, obj):
        return obj.user.email if obj.user else 'N/A'
    get_email.short_description = 'Email Address'


# Register your models here.




admin.site.register(Tender)