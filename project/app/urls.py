from django.urls import path
from . import views
from .views import GetSendInformationCreateView


urlpatterns = [
    # templates
    path("", views.index, name="index"),
    path("create/",GetSendInformationCreateView.as_view(),name='get-send-create'),
    path('toggle/', views.toggle_view, name='toggle'),
]