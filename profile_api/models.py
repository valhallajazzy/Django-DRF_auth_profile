from django.db import models


class User(models.Model):
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    code = models.DecimalField(max_digits=4, decimal_places=0, default=None,
                               blank=True, null=True, verbose_name='Код авторизации')
    shared_invite_code = models.CharField(max_length=6, unique=True, null=True,
                                          default=None, verbose_name='Код для приглашения друзей')
    friend_invite_code = models.CharField(max_length=6, null=True,
                                          default=None, verbose_name='Пригласительный код друга')
    is_active = models.BooleanField(default=False)
