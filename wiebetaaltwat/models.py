from django.db import models


class Participant(models.Model):
    wbw_id = models.CharField(unique=True, max_length=40)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
