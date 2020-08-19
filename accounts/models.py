from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create User Profile
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_country = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username

# Football Fan Information
SIZE_CHOICES = (
    ('Small','S'),
    ('Medium', 'M'),
    ('Large','L'),
    ('Extra Large','XL'),
    )

class UserFootball(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    club = models.CharField(max_length=20, null=True, blank=True)
    favorite_player = models.CharField(max_length=200, null=True, blank=True)
    favorite_shirts = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=12, choices=SIZE_CHOICES, blank=True, default='Medium')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile for all new users
    """

    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

    """
    Create a user fan profile for all new users
    """
    if created:
        UserFootball.objects.create(user=instance)
    # Existing users: just save the user fan info
    instance.userfootball.save()
