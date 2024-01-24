import csv
from matches.models import Match
from players.models import Player
from datetime import datetime


def handle_uploaded_file(matches, players, stats):
    decoded_players = players.read().decode("utf-8")
    decoded_matches = matches.read().decode("utf-8")
    decoded_stats = stats.read().decode("utf-8")
    reader_players = csv.DictReader(decoded_players.splitlines())
    reader_matches = csv.DictReader(decoded_matches.splitlines())
    reader_stats = csv.DictReader(decoded_stats.splitlines())

    for row in reader_players:
        if row["birthdate"] == "":
            row["birthdate"] = "1900-01-01"
            Player.objects.create(
            player_atp=row["player_id"],
            name=row["name"],
            hand=row["hand"],
            country=row["country"],
            birthdate=datetime.strptime(row["birthdate"], "%Y-%m-%d"),
        )

    for row in reader_matches:
            Match.objects.create(
            match_atp=row["match_id"],
            tournament=row["tournament"],
            date=datetime.strptime(row["date"], "%Y-%m-%d"),
            round=row["round"],
            duration=row["duration"],
        )

    for row in reader_stats:
        player = row["player_id"]
        match = Match.objects.get(match_atp=row["match_id"])
        if row["winner"] == "TRUE":
            winner = Player.objects.get(player_atp=player)
            match.winner = winner
        else:
            loser = Player.objects.get(player_atp=player)
            match.loser = loser
        match.save()
