from django.contrib import admin
from .models import get_information, send_information

# register a models in admin panel
admin.site.register(get_information)
admin.site.register(send_information)
