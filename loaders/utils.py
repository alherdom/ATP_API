from csv import DictReader
from matches.models import Match
from players.models import Player
from datetime import datetime


def handle_uploaded_players(players):
    decoded_players = players.read().decode("utf-8")
    reader_players = DictReader(decoded_players.splitlines())

    for row in reader_players:
        # if row["birthdate"] == "":
        #     row["birthdate"] = "1900-01-01"
        Player.objects.create(
            player_atp=row["player_id"],
            name=row["name"],
            hand=row["hand"],
            country=row["country"],
            birthdate=datetime.strptime(row["birthdate"], "%Y-%m-%d"),
        )


def handle_uploaded_matches(matches):
    decoded_matches = matches.read().decode("utf-8")
    reader_matches = DictReader(decoded_matches.splitlines())

    for row in reader_matches:
        Match.objects.create(
            match_atp=row["match_id"],
            tournament=row["tournament"],
            date=datetime.strptime(row["date"], "%Y-%m-%d"),
            round=row["round"],
            duration=row["duration"],
        )


def handle_uploaded_stats(stats):
    decoded_stats = stats.read().decode("utf-8")
    reader_stats = DictReader(decoded_stats.splitlines())

    for row in reader_stats:
        player = row["player_id"]
        match = Match.objects.get(match_atp=row["match_id"])
        if row["winner"] == "TRUE":
            match.winner = Player.objects.get(player_atp=player)
        match.loser = Player.objects.get(player_atp=player)
        match.save()
