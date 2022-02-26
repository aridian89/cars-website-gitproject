from django.contrib import admin
from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('thumbnail','model','year','color','milage','is_featured')
    list_display_links = ('model','thumbnail')
    search_fields = ('model','year')
    list_filter = ('model','is_featured')
    list_editable = ('is_featured',)
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:10px" />'.format(object.feature_image.url))
    thumbnail.short_description = 'Image'
admin.site.register(Car, CarAdmin)
