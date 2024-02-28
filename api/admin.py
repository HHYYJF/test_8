from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    exclude = ('bool',"currency")

admin.site.register(Item, ItemAdmin)