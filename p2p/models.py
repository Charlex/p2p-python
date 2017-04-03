import json
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class P2PUserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name="p2p_profile")
    groups = models.TextField()
    token = models.CharField(max_length=500)

    def get_markets(self):
        groups = json.loads(self.groups)
        markets = set()
        for group in groups:
            # subgroups will look something like ['p2p', 'content', 'lanews', 'edit']
            subgroups = group.split('.')
            if len(subgroups) >= 3 and subgroups[0] == "p2p" and subgroups[1] == "content":
                markets.add(subgroups[2])
        return markets


@receiver(post_save, sender=User)
def create_p2p_user_profile(sender, instance, created, **kwargs):
    if created or not instance.p2p_profile:
        P2PUserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_p2p_user_profile(sender, instance, **kwargs):
    if not instance.p2p_profile:
        P2PUserProfile.objects.create(user=instance)
