# Описание
Тестовое задание для [Хакатона по созданию мессенджера в Mail.ru](https://park.mail.ru/blog/topic/view/9407/).
Асинхронный сервер на Python 3, порт задается аргументом командной строки. 
По запросу из строки браузера вида: localhost:xxxx/get/file_name возвращает файл с именем file_name из рабочей директории
или ошибку, если такого файла нет.

# Установка
Для запуска сервера необходимо установить Python версии не ниже 3.5.
Затем запустить сервер из терминала:
```bash
python3 server.py PORT
```
PORT - обязательный аргумент.

# Использование
Перейти в браузере по адресу localhost:PORT/get/file_name. Вы увидите содержимое файла в текстовом виде.

# Пример выполнения
При запуске сервера можно посмотреть код сервера, перейдя по ссылке [http://localhost:8080/get/server.py](http://localhost:8080/get/server.py):
```
from aiohttp import web
import os
import argparse
import http


PATH = os.path.abspath(os.path.curdir)


def create_parser():
    parser = argparse.ArgumentParser(description='Set PORT for async server.')
    parser.add_argument('port', type=int, default=8080, help='PORT number for server')
    return parser

async def handle(request):
    file_name = request.match_info.get('file_name', "None")
    try:
        with open("{}/{}".format(PATH, file_name), 'r') as file:
            return web.Response(text=file.read())
    except FileNotFoundError:
        return web.HTTPInternalServerError()


app = web.Application()
app.router.add_get('/get/{file_name}', handle)

parser = create_parser()
args = parser.parse_args()

web.run_app(app, port=args.port)
```
