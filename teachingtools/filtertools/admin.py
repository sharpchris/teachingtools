from django.contrib import admin

# Register your models here.

from .models import Tool, Category, Screenshot

class ScreenshotAdmin(admin.TabularInline):
    model = Screenshot
    extra = 1

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('title','use_case')
    inlines = [ScreenshotAdmin]

    #TODO: Protect the slug field from editing after being created

@admin.register(Category)
class CategorytAdmin(admin.ModelAdmin):
    list_display = ('verbose_name',)
    fields = ('verbose_name', 'tooltip', 'option')
    ordering = ('verbose_name',)


