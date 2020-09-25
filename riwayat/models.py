from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.conf import settings

# Create your models here.


class Riwayat (models.Model):
    title = models.CharField(_("judul"), max_length=100)
    description = models.TextField(_("deskripsi"))
    image = models.ImageField(_("gambar"), upload_to='riwayat')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)
    time = models.DateTimeField(_("waktu"), auto_now=False, auto_now_add=False)

    def get_absolute_url(self):
        return reverse("riwayat:list")
