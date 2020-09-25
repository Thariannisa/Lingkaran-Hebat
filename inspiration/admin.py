from django.contrib import admin
from .models import Like, Clap, Inspiration
# Register your models here.
admin.site.register(Inspiration)
admin.site.register(Like)
admin.site.register(Clap)
