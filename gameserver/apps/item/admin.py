from django.contrib import admin

from apps.item.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "stackable")
    list_filter = ("name", "description", "stackable")
    search_fields = ("name", "description", "stackable")
