from django.shortcuts import render
from datetime import datetime


# создаем view, который принимает request и
# выводит некоторый текст на экран с помощью HttpResponse
# и передаем функцию в urls.py
# и добавляем подключение адресов в urls.py проекта

# теперь можем поменять на функцию render,
# которая первым аргументом принимает request,
# a 2 'web/main/html' и на страничку приходит html код
# передаем год в шаблон ( данные в шаблоне - контекст),
# и ключи становятся доступны для вывода

def main_view(request):
    year = datetime.now().year
    return render(request, 'web/main/html', {
        "year": year
    })
