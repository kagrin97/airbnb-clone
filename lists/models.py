from django.db import models
from core import models as core_models

class List(core_models.TimeStampedModel):

    """  List Model Definiton """

    name = models.CharField(max_length=80)
    user = models.OneToOneField("users.User", related_name="list", on_delete=models.CASCADE)
    room = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.room.count()

    count_rooms.short_description = "Number of Rooms"