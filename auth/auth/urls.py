from django.contrib import admin
# Импортируем модуль path для создания пути к веб-странице.
# Импортируем модуль include, для дальнейшего использования пути.
from django.urls import path, include
# Переход к страницам:
urlpatterns = [
    # По пути admin/.
    path('admin/', admin.site.urls),
    # По пути api/.
    path('api/', include('users.urls')),
]
