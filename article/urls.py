from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.MainPageView.as_view()),
    path('put/<int:obj_id>/', views.MainPageView.as_view()),
    path('<int:obj_id>', views.MainPageView.as_view()),
    # path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),
    path('<int:category_id>/',views.LowerCategoryView.as_view()),
    path('comment/<int:obj_id>/', views.CommentView.as_view()),
    path('like/<int:obj_id>', views.LikeView.as_view()),
    path('topicbest/', views.LowerTopicBestView.as_view()),
    path('count/<int:obj_id>', views.Count.as_view()),
    path('detail/<int:obj_id>/', views.DetailView.as_view()),
]


