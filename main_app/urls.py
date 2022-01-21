from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('widgets/create/', views.WidgetCreate.as_view(), name='widgets_create')
]