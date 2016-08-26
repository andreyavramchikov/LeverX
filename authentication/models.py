from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError(u'Users must have a valid email address.')

        account = self.model(email=self.normalize_email(email))

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.user_type = User.MANAGER
        account.save()

        return account


class User(AbstractBaseUser):
    DEVELOPER = 'DEVELOPER'
    MANAGER = 'MANAGER'
    USER_TYPE_CHOICES = (
        (DEVELOPER, 'DEVELOPER'),
        (MANAGER, 'MANAGER'),
    )
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    user_type = models.CharField(max_length=40, choices=USER_TYPE_CHOICES, default=DEVELOPER)

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __unicode__(self):
        return self.email

    @property
    def is_staff(self):
        return self.user_type == User.MANAGER

    def has_module_perms(self, app_label):
        return self.user_type == User.MANAGER

    def has_perm(self, perm, obj=None):
        return self.user_type == User.MANAGER

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

