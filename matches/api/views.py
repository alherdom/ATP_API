from rest_framework import generics
from matches.models import Match
from matches.api.serializers import MatchSerializer


class MatchListView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchDetailView(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchWinnerView(generics.ListAPIView):
    serializer_class = MatchSerializer

    def get_queryset(self):
        winner = self.kwargs["winner"]
        return Match.objects.filter(winner=winner)


class MatchLoserView(generics.ListAPIView):
    serializer_class = MatchSerializer

    def get_queryset(self):
        loser = self.kwargs["loser"]
        return Match.objects.filter(loser=loser)
