from django.contrib import admin

from apps.clan.models import Clan, ClanMember


@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "nivel")
    list_filter = ("name", "description", "nivel")
    search_fields = ("name", "description", "nivel")


@admin.register(ClanMember)
class ClanMemberAdmin(admin.ModelAdmin):
    list_display = ("character", "clan", "title")
    list_filter = ("character", "clan", "title")
    search_fields = ("character", "clan", "title")
