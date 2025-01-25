from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('extractor.urls')),  # Подключаем приложение extractor к корневому URL
]
