from django.contrib import admin
from books import models

admin.site.register(models.Author)
admin.site.register(models.Book)
