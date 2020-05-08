from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_mvp')
    list_editable = ('is_mvp',)
    search_fields = ('id', 'name', 'email', 'phone')
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
