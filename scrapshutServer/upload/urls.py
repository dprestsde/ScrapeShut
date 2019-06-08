from django.urls import path
from .views import *

urlpatterns = [
    path('', FileUploadView.as_view()),
    path('api/', UploadAPIView.as_view()),
    path('api/<int:pk>/', UploadDetailAPIView.as_view()),
    ]