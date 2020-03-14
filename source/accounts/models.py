from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='User')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Avatar')


    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
