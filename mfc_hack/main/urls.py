from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.start_window),
    path('info', views.info)

]