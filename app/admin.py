from django.contrib import admin
from .models import Item, Bill
# Register your models here

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Bill)
class ItemAdmin(admin.ModelAdmin):
    pass

