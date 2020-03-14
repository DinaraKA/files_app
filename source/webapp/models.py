from django.contrib.auth.models import User
from django.db import models

ACCESS_CHOICES = (
    ('base', 'Общий'),
    ('hidden', 'Скрытый'),
    ('private', 'Приватный'),
)

class File(models.Model):
    file = models.FileField(upload_to='files', verbose_name='Файл')
    name = models.CharField(max_length=20, verbose_name='Название')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, related_name='file_author', null=True, blank=True, default=None)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    access = models.CharField(max_length=20, default=ACCESS_CHOICES[0][0], verbose_name='Доступ', choices=ACCESS_CHOICES)

    def __str__(self):
        return self.name


class Private(models.Model):
    file = models.ForeignKey('File', on_delete=models.CASCADE, related_name='privates')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='private_access')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Приват'
        verbose_name_plural = 'Приват'
