from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nivel_global = models.PositiveIntegerField(default=1)
    xp_total = models.PositiveBigIntegerField(default=0)
    atributos_base = models.JSONField(default=dict)
    legacy_sports = models.JSONField(default=list)
    last_training = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Nivel {self.nivel_global}"