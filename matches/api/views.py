from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from matches.models import Match
from players.models import Player
from matches.api.serializers import PlayerSerializer, MatchSerializer


class PlayerListView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetailView(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = PlayerSerializer


class MatchListView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchDetailView(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchWinnerView(APIView):
    def get(self, request, pk):
        match = Match.objects.get(pk=pk)
        winner = match.winner
        serializer = PlayerSerializer(winner)
        return Response(serializer.data)


class MatchLoserView(APIView):
    def get(self, request, pk):
        match = Match.objects.get(pk=pk)
        loser = match.loser
        serializer = PlayerSerializer(loser)
        return Response(serializer.data)
