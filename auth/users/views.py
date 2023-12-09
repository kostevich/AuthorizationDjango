
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer


import datetime
import jwt

#==========================================================================================#
# >>>>> РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ <<<<< #
#==========================================================================================#

class Registerview(APIView):
    # Функция получения и добавления информации.
    def post(self, request):
        # Передача данных из запроса request.
        serializer = UserSerializer(data=request.data)

        # Проверка, действительна ли функция.
        serializer.is_valid(raise_exception=True)

        # Сохранение пользователя.
        serializer.save()

        # Возвращаем ответ сериализатора и данные пользователя.
        return Response(serializer.data)

#==========================================================================================#
# >>>>> ВХОД ПОЛЬЗОВАТЕЛЯ В СИСТЕМУ <<<<< #
#==========================================================================================#

class Loginview(APIView):
    def post(self, request):
        # Извлечение введенных данных в поле email.
        email = request.data['email']
        # Извлечение введенных данных в поле password.
        password = request.data['password']

        # Фильтрация введенных данных пользователем в базе данных.
        user = User.objects.filter(email=email).first()

        # Если email пользователя не найден в базе данных.
        if user is None:
            # Вывод ошибки аутентификации: пользователь не существует.
            raise AuthenticationFailed("Пользователя не существует")
        
        # Установим значения для токена:
        payload = {
            # id пользователя.
            'id': user.id,
            # Время жизни токена.
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24),
            # Время создания токена.
            'iat': datetime.datetime.utcnow()
        }

        # Создадим токен для пользователя.
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        # Сохраняем ответ в переменную response.
        response = Response()

        # Добавим данные ответа в файлы cookie, используем httponly для защиты файлов извне.
        response.set_cookie(key='jwt', value=token, httponly=True)

        # Данные ответа равны нашему токену.
        response.data = {'jwt': token}

        # Возвращаем токен в файле cookie.
        return response
    
#==========================================================================================#
# >>>>> ПОЛЬЗОВАТЕЛЬСКИЙ ИНТЕРФЕЙС <<<<< #
#==========================================================================================#

class UserView(APIView):
    def get(self, request):
        # Получение токена из файла cookie.
        token = request.COOKIES.get('jwt')
        # Если токен не найден в файле cookie.
        if not token:
            # Вывод ошибки аутентификации: пользователь не прошел авторизацию.
            raise AuthenticationFailed('Пользователь не прошел авторизацию.')
        # Попробуем декодировать токен.
        try:
            # Декодируем токен.
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        # Если не получилось: исключение.
        except jwt.ExpiredSignatureError:
            # Вывод ошибки аутентификации: пользователь не прошел авторизацию.
            raise AuthenticationFailed('Пользователь не прошел авторизацию.')
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
#==========================================================================================#
# >>>>> ВЫХОД ПОЛЬЗОВАТЕЛЯ ИЗ СИСТЕМЫ <<<<< #
#==========================================================================================#

class LogoutView(APIView):
    def post(self, request):
        # Получаем ответ в переменную response.
        response = Response()

        # Удаляем токен их файлов cookies.
        response.delete_cookie('jwt')

        # Сохраняем в базу данных успешный выход их системы.
        response.data = {'Сообщение': 'Выход пользователя прошел успешно.'}

        # Возвращаем сообщение об удачном выходе.
        return response
