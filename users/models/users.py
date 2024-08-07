from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save

from users.models.profile import Profile


class User(AbstractUser):
    username = models.CharField(
        'Никнейм', max_length=64, unique=True, null=True, blank=True
    )
    email = models.EmailField('Почта', unique=True, null=True, blank=True)
    phone_number = PhoneNumberField(
        'Телефон', unique=True, null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователь'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.phone_number}"

# NOTE - профиль создаётся при создании пользователя автоматически, такое же можно сделать и через get_or_create


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)
