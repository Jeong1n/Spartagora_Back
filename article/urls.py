from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.MainPageView.as_view()),
    path('<int:obj_id>', views.MainPageView.as_view()),
    path('delete/<int:obj_id>', views.MainPageView.as_view()),
    path('<int:category_id>/',views.LowerCategoryView.as_view()),
]


