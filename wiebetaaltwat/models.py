from django.db import models


class Participant(models.Model):
    wbw_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
