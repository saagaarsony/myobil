# In MainApp/admin.py
from django.contrib import admin
from MainApp.models import Bus_Details, Per_Details

class PerDetailsAdmin(admin.ModelAdmin):
    model = Per_Details
    verbose_name = "Custom Person Detail"
    verbose_name_plural = "Custom Person Details"

class BusDetailsAdmin(admin.ModelAdmin):
    model = Bus_Details
    verbose_name = "Custom Bus Detail"
    verbose_name_plural = "Custom Bus Details"

admin.site.register(Per_Details, PerDetailsAdmin)
admin.site.register(Bus_Details, BusDetailsAdmin)