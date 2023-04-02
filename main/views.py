from django.shortcuts import render

def index(request): # Всегда нужно отправлять request (запрос)
    data = {
        'title': 'Главная страница',
        # 'values': ['Some', 'Hello', '123'],
        # 'obj': {
        #     'car' : 'BMW',
        #     'age' : '18',
        #     'hobby' : 'Football'
        # }
    }
    # файл всегда указывается с учетом того, что мы находимся в папке templates
    return render(request, 'main/index.html', data) # render показывает полностью html шаблон при переходе на страницу

