from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, timedelta
from django.conf import settings

# Supabase Initialization moved to utils.py
from .utils import supabase_client

class User(AbstractUser):
    reset_token = models.CharField(max_length=255, null=True, blank=True)
    token_expiration = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=255, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group', related_name='tourism_app_user_groups', blank=True, help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='tourism_app_user_permissions', blank=True, help_text='Specific permissions for this user.'
    )

    def generate_reset_token(self):
        self.reset_token = supabase_client.auth.api.generate_link("recovery", self.email)["action_link"]
        self.token_expiration = datetime.now() + timedelta(hours=1)
        self.save()

    def generate_verification_token(self):
        self.verification_token = supabase_client.auth.api.generate_link("signup", self.email)["action_link"]
        self.save()

class Explore(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Destination', 'Destination'),
        ('Event', 'Event'),
        ('Activity', 'Activity'),
    ]
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='explore_images/')
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    class Meta:
        verbose_name_plural = "Explores"

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image:
            return settings.MEDIA_URL + str(self.image)
        return None

class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    explore = models.ForeignKey(Explore, on_delete=models.CASCADE)
    search_image = models.URLField()
    search_title = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.search_image = self.explore.image_url
        self.search_title = self.explore.title
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} searched {self.search_title}"
