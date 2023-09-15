from django.contrib import admin

from apps.character.models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "nivel")
