from django.contrib import admin

from apps.inventary.models import Inventary


@admin.register(Inventary)
class InventaryAdmin(admin.ModelAdmin):
    list_display = ("character", "item", "quantity", "equipped")
    list_filter = ("character", "item", "equipped")
    search_fields = ("character", "item", "equipped")
