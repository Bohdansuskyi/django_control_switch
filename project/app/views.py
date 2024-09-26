# for templates
from django.shortcuts import render, redirect
from .models import get_information, send_information

#django rest_framework (API)
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import GetInformationSerializer, SendInformationSerializer
from rest_framework.views import APIView

# view for template
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

# switch function
def toggle_view(request):
    if request.method == 'POST':
        last_record = send_information.objects.last()

        # Перевіряємо чи є останній запис, якщо ні, значення True
        new_active_value = not last_record.send_value if last_record else True

        # Створюємо новий запис зі зміненим станом
        send_information.objects.create(send_value=new_active_value)

        # Після створення нового запису, робимо редирект на головну сторінку
        return redirect('index')

# API

class GetSendInformationCreateView(APIView):

    # GET: отримати get_value і вислати send_value
    def get(self, request):
        # Отримуємо параметр get_value з URL
        get_value = request.GET.get('get_value')

        if get_value:
            # Логіка для обробки даних
            data = {
                'get_value': get_value,
            }

            serializer = GetInformationSerializer(data=data)

            if serializer.is_valid():
                # Зберігаємо get_value у базу даних
                serializer.save()

                # Отримуємо останнє значення send_value
                last_send_value = send_information.objects.last()

                if last_send_value:
                    send_value = last_send_value.send_value
                else:
                    send_value = False  # Значення за замовчуванням, якщо даних немає

                # Відповідаємо разом із send_value
                return Response({
                    'send_value': send_value
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": "get_value is required."}, status=status.HTTP_400_BAD_REQUEST)
