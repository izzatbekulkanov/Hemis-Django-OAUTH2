from django.db import models

class UserProfile(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    picture = models.URLField()
    # Boshqalar uchun kerakli qismlar shu joyga qo'shiladi

    def __str__(self):
        return self.name