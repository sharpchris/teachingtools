from django.contrib import admin

# Register your models here.

from .models import Tool, Category

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('title','use_case')

@admin.register(Category)
class CategorytAdmin(admin.ModelAdmin):
    list_display = ('verbose_name',)
    fields = ('verbose_name', 'tooltip', 'option')
    ordering = ('verbose_name',)


