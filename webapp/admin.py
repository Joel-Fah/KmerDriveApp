from django.contrib import admin
from .models import ContactInfo, UserProfileInfo

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'message']
    search_fields = ['name']
    
class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'last_modified', 'phone', 'vehiculated', 'about']
    search_fields = ['phone']
    list_filter = ['vehiculated']

admin.site.register(ContactInfo, ContactAdmin)
admin.site.register(UserProfileInfo, UserProfileInfoAdmin)