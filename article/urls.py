from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view()),
    path('<int:obj_id>', views.MainPageView.as_view()),
    path('delete/<int:obj_id>', views.MainPageView.as_view()),
]

