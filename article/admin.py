from django.contrib import admin
from .models import Article,Comment,UpperCategory,LowerCategory
# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(UpperCategory)
admin.site.register(LowerCategory)



