from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Festival)
admin.site.register(models.Comment)
admin.site.register(models.Movie)
admin.site.register(models.Actor)
admin.site.register(models.Award)
admin.site.register(models.Producent)