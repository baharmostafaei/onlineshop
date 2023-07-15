from django.contrib import admin
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime_created',)

admin.site.register(models.Product, ProductAdmin)
    
