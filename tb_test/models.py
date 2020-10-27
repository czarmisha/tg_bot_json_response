from django.db import models


class TgUser(models.Model):
    username = models.CharField(max_length=155, verbose_name='Username')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
