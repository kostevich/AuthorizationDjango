# Импортируем модуль APIView для создания представлений.
from rest_framework.views import APIView
# Импортируем класс UserSerializer для преобразования данных.
from .serializers import UserSerializer
# Импортируем модуль Response для обработки запросов.
from rest_framework.response import Response
# Импортируем молдель User, для проверки данных при входе в систему.
from .models import User
# Используем модуль, для вывода ошибки авторизации.
from rest_framework.exceptions import AuthenticationFailed


# Создадим класс регистрации Registerview.
class Registerview(APIView):
    # Функция получения и добавления информации.
    def post(self, request):
        # Передача данных из запроса request.
        serializer = UserSerializer(data=request.data)
        # Проверка, действительна ли функция.
        serializer.is_valid(raise_exception=True)
        # Сохранение пользователя
        serializer.save()
        # Возвращаем ответ сериализатора и данные пользователя.
        return Response(serializer.data)


# Создадим класс входа в систему LoginView.
class Loginview(APIView):
    # Функция получения и проверки информации.
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
        # Если email пользователя и пароль не совпадает с базой данных.
        # if not user.check_password(password):
        #     # Вывод ошибки аутентификации: неверный пароль.
        #     raise AuthenticationFailed('Неверный пароль')
        # Возвращаем пользователя.
        return Response({'message':'Вход выполнен'})
