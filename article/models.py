from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.


class Article(models.Model):
    title = models.CharField(_("judul"), max_length=255)
    image = models.ImageField(_("gambar"), upload_to='article/', null=True)
    time = models.DateTimeField(_("waktu"), auto_now=True, auto_now_add=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)
    countLike = models.IntegerField(_("Like"), null=True)
    countClap = models.IntegerField(_("Clap"), null=True)


class Likes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)
    article = models.ForeignKey(
        Article,  on_delete=models.CASCADE, default=1)


class Claps(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)
    article = models.ForeignKey(
        Article,  on_delete=models.CASCADE, default=1)
