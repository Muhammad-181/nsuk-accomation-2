from django.contrib import admin
from .models import Instituition, Property, Image, Location
import django_filters

# Register your models here.
admin.site.register(Location)
admin.site.register(Instituition)


class ImageAdmin(admin.StackedInline):
    model = Image

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ( 'user', 'instituition', 'location', 'status', 'created_at',)
    list_filter = ('user', 'status', 'location', 'instituition', 'created_at',)
    search_fields = ['title', 'content',]

    class Meta:
        model = Property

@admin.register(Image)
class ImagaAdmin(admin.ModelAdmin):
    pass



class PropertyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ( 'user', 'instituition', 'status', 'created_at',)
    list_filter = ('user', 'status', 'instituition',)
    search_fields = ['title', 'content',]