from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category_list),
    path('category/<int:pk>/', views.category_detail),
    path('tag/', views.tag_list),
    path('tag/<int:pk>/', views.tag_detail),
    path('post/', views.post_list),
    path('post/<int:pk>', views.post_detail),
    path('comment/', views.comment_list),
    path('commetn/<int:pk>', views.comment_detail),
]