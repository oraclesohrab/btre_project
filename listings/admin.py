from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'state', 'is_published')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('city', 'state')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
