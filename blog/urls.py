from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.base, name='base'),
    # post_id 가 views.detail의 인자로 넘어감
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
