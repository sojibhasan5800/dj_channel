from django.db import models
from django.contrib.auth.models import User

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your models here.

class Game(models.Model):
    room_code = models.CharField(max_length=100)
    game_creator = models.CharField(max_length=100)
    game_opponent = models.CharField(max_length=100 , blank=True , null=True)
    is_over = models.BooleanField(default=False) 