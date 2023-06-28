# Импортируем модуль path для создания пути к веб-странице.
from django.urls import path
# Импортируем класс Registerview, Loginview, UserView для создания пути к веб-странице.
from .views import Registerview, Loginview, UserView, LogoutView

# Переход к страницам
urlpatterns = [
    # По пути admin/
    path('register', Registerview.as_view()),
    path('login', Loginview.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]
