from . import views
from .views import GetPosts, GetDetail, CreatePost, UpdateView, UpdatePost, DeletePost, UpdatePost, DeletePost, index

from django.urls import path


urlpatterns = [
    path('', GetPosts.as_view(), name='home'),
    path('detail/<int:pk>', GetDetail.as_view(), name='detail'),
    path('create', CreatePost.as_view(), name='create'),
    path('update/<int:pk>', UpdatePost.as_view(), name='update'),
    path('delete/<int:pk>', DeletePost.as_view(), name='delete'),
    path('test', index),
    path('upload/', views.image_upload_view)

]
