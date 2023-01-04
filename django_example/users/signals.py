from django.db.models.signals import post_save # Fires after a object is saved
from django.contrib.auth.models import User
from django.dispatch import receiver # Receiver gets signal and performs task. Decorator
from .models import Profile

# When User is saved send signal
# Get post_save signal when user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs): #kwargs accepts additional keyword arguments. post save signal sends argurments. instance is instance of user created
    if created:
        Profile.objects.create(user=instance)

# If User is saved also save the profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()