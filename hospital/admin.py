from django.contrib import admin

from .models import Hospital

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name','email','capacity']
    search_fields = ['name','email',]
    list_per_page = 10
