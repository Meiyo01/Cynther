from django.contrib import admin
from .models import Government, Empire, Clan

@admin.register(Government)
class GovernmentAdmin(admin.ModelAdmin):
    list_display = 'name', 'monarch', 'formed', 'status'
    list_filter = 'name', 'monarch', 'formed', 'status'
    search_fields = 'name', 'monarch', 'info'

@admin.register(Empire)
class EmpireAdmin(admin.ModelAdmin):
    list_display = 'name', 'formed', 'strength', 'status'
    list_filter = 'name', 'formed', 'strength', 'reputation', 'government', 'platform'
    search_fields = 'name', 'monarch', 'bio'

@admin.register(Clan)
class ClanAdmin(admin.ModelAdmin):
    list_display = 'name', 'formed', 'strength', 'status'
    list_filter = 'name', 'formed', 'strength', 'reputation', 'government', 'platform'
    search_fields = 'name', 'monarch', 'bio'

