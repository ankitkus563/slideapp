from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.test),
    path('slides/<int:file_id>/',views.slide_form_view),
    path('update/<int:file_id>/',views.update),
    path('delete/<int:file_id>/',views.delete)
]