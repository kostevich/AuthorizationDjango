# Импортируем модуль path для создания пути к веб-странице.
from django.urls import path
# Импортируем класс Registerview для создания пути к веб-странице.
from .views import Registerview
# Импортируем класс Loginview для создания пути к веб-странице.
from .views import Loginview

# Переход к страницам
urlpatterns = [
    # По пути admin/
    path('register', Registerview.as_view()),
    path('login', Loginview.as_view()),
]
