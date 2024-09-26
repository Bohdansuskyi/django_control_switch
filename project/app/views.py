from django.shortcuts import render, redirect
from .models import get_information, send_information

def index(request):
    data = get_information.objects.last()
    
    if data:
        time_get = str(data.time_get)
        get_value = data.get_value
    else:
        time_get = None
        get_value = None

    if get_value == True:
        get_value = "ON"

    elif get_value == False:
        get_value = "OFF"

    return render(request, "app/index.html", {
        'time_get': time_get,
        'get_value': get_value
    })

def toggle_view(request):
    if request.method == 'POST':
        last_record = send_information.objects.last()

        # Перевіряємо чи є останній запис, якщо ні, значення True
        new_active_value = not last_record.send_value if last_record else True

        # Створюємо новий запис зі зміненим станом
        send_information.objects.create(send_value=new_active_value)

        # Після створення нового запису, робимо редирект на головну сторінку
        return redirect('index')
