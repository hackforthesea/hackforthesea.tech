from django.contrib.auth.models import User
from django.db.models.signals import pre_save

@receiver(pre_save, sender=User)
def user_inactive(sender, **kwargs):
    print("Request finished!")