from django.urls import path
from Main.views import MainView
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),

]