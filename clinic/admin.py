from django.contrib import admin
admin.site.site_header = 'MGN SCC'
# Register your models here.
from .models import Clinic
class ClinicAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'patient_phone', 'patient_address', 'patient_case', 'drug', 'fees', 'doctor', 'datetime']
    list_filter = ['patient_address', 'patient_case', 'doctor', 'drug', 'fees', 'datetime']
    search_fields = ['patient_name']

admin.site.register(Clinic, ClinicAdmin)   