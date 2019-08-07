from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.board, name="board"),
    path('<int:board_id>', views.detail3, name="detail3"),
    path('new', views.new3, name="new3"),
    path('create', views.create3, name="create3"),
    path('edit/<int:board_id>', views.edit3, name="edit3"),
    path('update/<int:board_id>', views.update3, name="update3"),
    path('delete/<int:board_id>', views.delete3, name="delete3"),
    path('comment/create/<int:board_id>', views.comment_create,name="comment_create"),
    path('like/<int:board_id>',views.post_like, name="post_like"), # like를 위한 url
]