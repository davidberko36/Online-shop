from django.contrib import admin

# Register your models here.
from .models import Category, Item

admin.site.register(Category)
admin.site.register(Item)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)