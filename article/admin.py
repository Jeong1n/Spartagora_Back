from xml.etree.ElementTree import Comment
from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Article)
admin.site.register(models.Comment)
admin.site.register(models.UpperCategory)
admin.site.register(models.LowerCategory)


