from django.urls import path
from . import views


urlpatterns = [
    # templates
    path("", views.index, name="index"),
    path('toggle/', views.toggle_view, name='toggle'),
]