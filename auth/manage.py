#!/usr/bin/env python

#==========================================================================================#
# >>>>> ПОДКЛЮЧЕНИЕ БИБЛИОТЕК И МОДУЛЕЙ <<<<< #
#==========================================================================================#

from dublib.Methods import CheckPythonMinimalVersion


import os
import sys

#==========================================================================================#
# >>>>> ИНИЦИАЛИЗАЦИЯ СКРИПТА <<<<< #
#==========================================================================================#

def main():
    # Проверка настроек
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'auth.settings')
    # Проверка импорта Django.
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    # Проверка поддержки используемой версии Python.
    CheckPythonMinimalVersion(3, 11)

# Ожидание запуска с командной строки Django.
if __name__ == '__main__':
    main()
