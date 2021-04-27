from django.urls import path
from .views import (BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView, BlogDeleteView)
from.views import *

urlpatterns = [

path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
path('post/<int:pk>/publish/', post_publish, name='post_publish'),
path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete' ),
path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'), # new
path('post/new/', BlogCreateView.as_view(), name='post_new'),
path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
path('', BlogListView.as_view(), name='home' ),

]