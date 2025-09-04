from django.db import models
from django.contrib.auth.models import User

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    notification = models.TextField(max_length=110)
    is_seen = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        print("savecalled")
        channel_layer = get_channel_layer()
        notification_obj = Notification.objects.filter(is_seen = False).count()
        data = {'count':notification_obj,'curr':self.notification}
        
        async_to_sync(channel_layer.group_send)(
            'test_consumer_group',{
                'type':'send_notification',
                'value':data
            }
        )

        super(Notification,self).save(*args,**kwargs)



