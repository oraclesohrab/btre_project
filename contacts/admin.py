from django.contrib import admin
from .models import Contact


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'listing', 'contact_time',)
    list_filter = ('listing',)
    search_fields = ('listing', 'email')
    list_per_page = 25


admin.site.register(Contact, ContactsAdmin)
