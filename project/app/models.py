from django.db import models

# models for creating database

class get_information(models.Model):
    get_value = models.BooleanField()
    time_get = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
    
class send_information(models.Model):
    send_value = models.BooleanField()
    time_send = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)