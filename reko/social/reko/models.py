from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Let's create a user profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # We'll associate one user to one profile, and if User gets deleted, delete "profile" too
    follows = models.ManyToManyField("self",
        related_name="followed_by", # Ppl who follows you
        symmetrical=False, # If you follow someone, that someone doesn't have to follow you, right?
        blank=True) # I mean it would be cool if you started following me... <3 see ya there boi / Yeah but you start following nothing...

    date_modified = models.DateTimeField(User, auto_now=True) # When was this profile last modified?

    def __str__(self):
        return self.user.username

# Create a Profile when a new user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        # have the user followed themselves
        user_profile.follows.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User) # When a new user is created, call create_profile
# https://youtu.be/H8MmNqDyra8?si=GBYUTRJDP1OOcH7W&t=488