from django.urls import path
from . import views
from django.conf import settings


urlpattern = [
    path('',views.LowerCategoryView.as_view()),
]