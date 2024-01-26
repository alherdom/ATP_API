from django.urls import path
from . import views

app_name = "matches"

urlpatterns = [
    path("api/matches/", views.MatchListView.as_view(), name="matches_list"),
    path(
        "api/matches/<int:pk>/", views.MatchDetailView.as_view(), name="matches_detail"
    ),
    path(
        "api/matches/winner/pk/<str:winner>/",
        views.MatchWinnerView.as_view(),
        name="matches_winner",
    ),
    path(
        "api/matches/loser/pk/<str:loser>/",
        views.MatchLoserView.as_view(),
        name="matches_loser",
    ),
]
