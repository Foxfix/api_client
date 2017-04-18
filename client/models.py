from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from decimal import Decimal

@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    """
    Make a client's account in inactive state after registration.
    """
    if not instance.is_superuser:
        if instance._state.adding is True:
            instance.is_active = False
        else:
            print("Updating User Record")


class Profile(models.Model):
    """ Profile user information. """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_information')
    balance = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    passport_number = models.CharField(max_length=15, default="BC123456")
    accaunt = models.BooleanField(default=True)
    
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.user_information.save()

