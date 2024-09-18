from django.contrib import admin
from app_menu.models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent')
    list_filter = ('name',)
    search_fields = ('name', 'url')
    ordering = ('name', 'id')
