from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_upload, name='image_upload'),  # Устанавливаем обработчик для корневого URL
]

