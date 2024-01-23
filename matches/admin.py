from django.contrib import admin
from .models import Match

admin.site.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("tournament", "date", "round", "duration", "winner", "loser")
    list_filter = ("tournament", "date", "round", "duration", "winner", "loser")
    list_editable = ("id", "tournament", "date", "round", "duration", "winner", "loser")
    search_fields = ("tournament", "date", "round", "duration", "winner", "loser")
    ordering = ("tournament", "date", "round", "duration", "winner", "loser")