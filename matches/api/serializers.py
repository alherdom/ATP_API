from rest_framework import serializers
from matches.models import Match
from players.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            "name",
            "hand",
            "country",
            "birthdate",
        ]


class MatchSerializer(serializers.ModelSerializer):
    winner = PlayerSerializer()
    loser = PlayerSerializer()

    class Meta:
        model = Match
        fields = ["tournament", "date", "round", "duration", "winner", "loser"]
