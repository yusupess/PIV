from django.contrib import admin
from .models import Part

class PartAdmin(admin.ModelAdmin):
    list_display = (
        'part_number',
        'name',
    )
    search_fields = ('name', 'part_number')
    list_filter = ('name',)

admin.site.register(Part, PartAdmin)
