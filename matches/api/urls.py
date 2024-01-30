from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path("players/",
         views.PlayerListView.as_view(),
         name="players_list"),
    path("players/<int:pk>/",
         views.PlayerDetailView.as_view(),
         name="players_detail"),
    path("matches/",
         views.MatchListView.as_view(),
         name="matches_list"),
    path("matches/<int:pk>/",
         views.MatchDetailView.as_view(),
         name="matches_detail"),
    path(
        "matches/<int:pk>/winner/",
        views.MatchWinnerView.as_view(),
        name="matches_winner",
    ),
    path(
        "matches/<int:pk>/loser/",
        views.MatchLoserView.as_view(),
        name="matches_loser",
    ),
]
