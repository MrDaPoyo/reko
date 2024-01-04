from django.db import models
from django.contrib.auth.models import User

# Let's create a user profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # We'll associate one user to one profile, and if User gets deleted, delete "profile" too
    follows = models.ManyToManyField("self",
    related_name="followed_by", # Ppl who follows you
    symmetrical=False, # If you follow someone, that someone doesn't have to follow you, right?
    blank=True) # I mean it would be cool if you started following me... <3 see ya there boi / Yeah but you start following nothing...