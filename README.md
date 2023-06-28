# Authorization_Django

____
## Обзор. 
**Authorization_Django** - скрипт на [Django](https://github.com/django/django), осуществляющий регистрацию, вход, просмотр информации о пользователе и выход из системы.

____
##  Условия для использования продукта.
1. Установить Python версии не старше [3.11](https://www.python.org/downloads/).

2. В среду исполнения инсталлировать пакеты **_Django, PyJWT==1.7.1_** или  использовать файл **_requirements.txt_**:

  **`pip install Django`**

  **`pip install PyJWT==1.7.1`**
  
  или 
  
  **`pip install -r /path/to/requirements.txt`**
  
3. Запустить сервер через терминал, предварительно указав исполняемую директорию методом `cd`.

**```python manage.py runserver```**.

4. Перейти по [ссылке](http://127.0.0.1:8000/api/).

5. Добавить к ссылке в зависимости от нужной функции:

* register

* login
  
* user
  
* logout
  
____
## Пример работы
**[Регистрация:](http://127.0.0.1:8000/api/register)**

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/5c0ed103-4f92-4a24-aa15-b562cb5cd655)

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/a20d97f2-e417-40e7-a6f5-ec3e214772ef)

**[Вход в систему:](http://127.0.0.1:8000/api/register)**

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/2181e424-6339-4714-8b26-6b354892c7c9)

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/4a1a86c9-8df5-4939-97f2-1d46c2bbdd46)

**[Данные пользователя:](http://127.0.0.1:8000/api/user)**

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/d27e3bdc-94e1-4733-8d9a-c0f006084cd7)

**[Выход из системы:](http://127.0.0.1:8000/api/logout)**

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/21f837d4-c349-4bb5-ba46-61afa803696e)

![image](https://github.com/kostevich/Authorization_Django/assets/109979502/0b6554a0-bc57-4b6b-bf44-3208dcf59496)

____
## Дополнительно.

Токен хранится в файлах cookies.
