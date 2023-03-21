from django.urls import path

#import TestTask.file_uploader.views
from file_uploader import views

urlpatterns = [
    path('upload/', views.Uploader.as_view(), name='upload')
]