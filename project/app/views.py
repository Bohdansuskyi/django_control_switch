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

    # get last data from database
    data = get_information.objects.last()
    
    # validate data
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

        # Check whether the last record is there, if not, the value is True
        new_active_value = not last_record.send_value if last_record else True

        # Create a new record with a changed state
        send_information.objects.create(send_value=new_active_value)

        # After creating a new record, redirect to the main page
        return redirect('index')

# API

class GetSendInformationCreateView(APIView):

    # GET: get get_value and send send_value
    def get(self, request):
        # Get the get_value parameter from the URL
        get_value = request.GET.get('get_value')

        if get_value:
            # Logic for data processing
            data = {
                'get_value': get_value,
            }

            serializer = GetInformationSerializer(data=data)

            if serializer.is_valid():
                # Store get_value in the database
                serializer.save()

                # Get the last value of send_value
                last_send_value = send_information.objects.last()

                if last_send_value:
                    send_value = last_send_value.send_value
                else:
                    send_value = False  # Default value if no data

                # Respond together with send_value
                return Response({
                    'send_value': send_value
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": "get_value is required."}, status=status.HTTP_400_BAD_REQUEST)
