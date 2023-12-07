
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from django.urls import path
from .views import Registerview, Loginview, UserView, LogoutView

#==========================================================================================#
# >>>>>  ЛОКАЛЬНЫЕ ССЫЛКИ ДЛЯ РАБОТЫ САЙТА <<<<< #
#==========================================================================================#

urlpatterns = [
    # По пути api/
    path('register', Registerview.as_view()),
    path('login', Loginview.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
]

