# AuthorizationDjango
**AuthorizationDjango** - учебный скрипт на [Django](https://github.com/django/django), осуществляющий регистрацию, вход, просмотр информации о пользователе и выход из системы.

# Порядок установки и использования.
1. Загрузить репозиторий. Распаковать. 
2. Установить [Python](https://www.python.org/downloads/) версии не старше 3.11. Рекомендуется добавить в PATH.
3. В среду исполнения установить следующие пакеты: [Django](https://github.com/django/django?ysclid=lph3fmn0za256973455), [djangorestframework](https://github.com/encode/django-rest-framework?ysclid=lpvej8gr5a512312386), [dublib](https://github.com/DUB1401/dublib), [PyJWT](https://github.com/jpadilla/pyjwt?ysclid=lpvehdtfmm948560978) не старше 1.7.1.
```
pip install Django
pip install djangorestframework
pip install git+https://github.com/DUB1401/dublib#egg=dublib
pip install PyJWT
```
Либо установить сразу все пакеты при помощи следующей команды, выполненной из директории скрипта.
```
pip install -r requirements.txt
```
4. В среде исполнения запустить файл _manage.py_ командой:
```
python manage.py runserver
```
5. Перейти по ссылке (пример: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)).

# Пример работы
**Регистрация:**

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/5c0ed103-4f92-4a24-aa15-b562cb5cd655)

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/a20d97f2-e417-40e7-a6f5-ec3e214772ef)

**Вход в систему:**

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/2181e424-6339-4714-8b26-6b354892c7c9)

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/4a1a86c9-8df5-4939-97f2-1d46c2bbdd46)

**Данные пользователя:**

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/d27e3bdc-94e1-4733-8d9a-c0f006084cd7)

**Выход из системы:**

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/21f837d4-c349-4bb5-ba46-61afa803696e)

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/0b6554a0-bc57-4b6b-bf44-3208dcf59496)

_Copyright © Kostevich Irina. 2023._
