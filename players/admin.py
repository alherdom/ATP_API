from django.contrib import admin
from .models import Player

admin.site.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "hand", "country", "birthdate")
    list_filter = ("hand", "country")
    list_editable = ("id", "name", "hand", "country", "birthdate")
    search_fields = ("name", "country")
    ordering = ("name", "country")
