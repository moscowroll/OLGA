from django.contrib import admin

from . import models

admin.site.register(models.Person)
admin.site.register(models.Question_1)
admin.site.register(models.Question_2)

# Register your models here.
