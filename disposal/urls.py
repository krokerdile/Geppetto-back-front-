from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.disposal, name="disposal"),
    path('<int:disposal_id>', views.detail2, name="detail2"),
    path('new', views.new2, name="new2"),
    path('create', views.create2, name="create2"),
    path('edit/<int:disposal_id>', views.edit2, name="edit2"),
    path('update/<int:disposal_id>', views.update2, name="update2"),
    path('delete/<int:disposal_id>', views.delete2, name="delete2"),
]+static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
