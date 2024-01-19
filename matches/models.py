from django.db import models
from players.models import Player

class Match(models.Model):
    tournament = models.CharField(max_length=200)
    date = models.DateField()
    round = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="winner")
    loser = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="loser")

    class Meta:
        indexes = [
            models.Index(fields=["tournament",]),
            models.Index(fields=["date",]),
            models.Index(fields=["round",]),
            models.Index(fields=["winner",]),
            models.Index(fields=["loser",]),
        ]
    
    def __str__(self):
        return self.tournament + " " + str(self.date) + " " + self.round + " " + str(self.winner) + " " + str(self.loser)