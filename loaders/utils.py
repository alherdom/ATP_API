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
        new_player = Player.objects.create(
            player_id=row["player_id"],
            name=row["name"],
            hand=row["hand"],
            country=row["country"],
            birthdate=datetime.strptime(row["birthdate"], "%Y-%m-%d"),
        )

    for row in reader_matches:
        new_match = Match.objects.create(
            match_id=row["match_id"],
            tournament=row["tournament"],
            date=datetime.strptime(row["date"], "%Y-%m-%d"),
            round=row["round"],
            duration=row["duration"],
        )
