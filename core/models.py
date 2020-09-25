from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email address'), unique=True)
    name = models.CharField(_('Name'), max_length=100, blank=True)
    avatar = models.ImageField(
        _('Gambar'), upload_to='avatar/', null=True, blank=True)
    umur = models.IntegerField(_("Umur"), null=True, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True)
    date_joined = models.DateTimeField(
        _('date joined'), editable=False, auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_absolute_url(self):
        return reverse("core:success", kwargs={'pk': self.id})

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
