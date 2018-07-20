# otus_web_django_market

Интернет-магазин, сделанный с использованием фреймворка Django

## Установка

С использованием git и установкой зависимостей из requirements.txt (для разработки):
```bash
1. Скачать исходный код веб-приложения
$ git clone https://github.com/nikolnikon/otus_web_django_market.git

2. Установить необходимые зависимости
$ cd otus_web_django_market
$ pip install -r requirements.txt

3. Создать базу данных
$ docker-compose up -d

4. Выполнить миграции
$ python manage.py migrate

5. Загрузить данные в БД
$ python manage.py loaddata 1_categories
$ python manage.py loaddata 2_products
```

## Запуск приложения
Данная иструкция распространяется на запуск приложения с помощью предоставляемого Django веб-сервера. Такой вариант не 
подходит для развертывания в "боевом" окружении. Подходы к развертыванию в "боевом" окружении описаны в документации.  
```bash
1. Создать в корневой директории (otus_web_django_market) файл .env

2. Прописать в нем переменные окружения, соответствующие натсройкам веб-приложения. По умолчанию значения настроек 
берутся из файла settings.py

3. Выполнить команду
$ python manage.py runserver --settings=django_market.settings --configuration=<configuration>
configuration - Dev или Prod (см. django_market.settings)
```

## Работа приложения
Страница со списком продуктов

![Список продуктов](https://i.gyazo.com/0425318a7bf7152c4f2e74ec1df49129.png)

Страница конкретного продукта

![Конкретный продукт. Описание](https://i.gyazo.com/906b0c6da0435ee0ad9304e9eea70c78.png)

![Конкретный продукт. Характеристики](https://i.gyazo.com/a2d8eb22b43794ad113d31bd65ac7ad6.png)

## Лицензия
Проект распространяентся под лицензией MIT. Подробная информация в файле
[LICENSE](https://github.com/nikolnikon/otus_web_django_market/blob/master/LICENSE)
