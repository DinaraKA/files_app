from django.contrib.auth.models import User
from django.db import models



# class Profile(models.Model):
#     user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='User')
#     avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Avatar')
#     about_user = models.TextField(max_length=2000, null=True, blank=True, verbose_name='About User')
#     github = models.URLField(null=True, blank=True, verbose_name='GitHub')


#     def __str__(self):
#         return self.user.get_full_name() + "'s Profile"

#     class Meta:
#         verbose_name = 'Profile'
#         verbose_name_plural = 'Profiles'
