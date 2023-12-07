
#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from rest_framework import serializers
from .models import User

#==========================================================================================#
# >>>>>  <<<<< #
#==========================================================================================#

class UserSerializer(serializers.ModelSerializer):
    # Класс Meta, конструирующий класс UserSerializer.
    class Meta:
        # Используем модель User.
        model = User

        # Используем поля модели User.
        fields = ['id', 'username', 'email', 'password']

        # Добавляем параметры просмотра поля password.
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            password = validated_data.pop('password', None)

            # Создаем экземпляр пользователя проверенными данными.
            instance = self.Meta.model(**validated_data)

            # Если пароль не пустой.
            if password is not None:
                instance.set_password(password)

            # Сохраняем экземпляр пользователя с валидными данными.
            instance.save()
            
            # Возвращаем экземпляр пользователя с валидными данными.
            return instance
