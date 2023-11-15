from django.urls import path
from . import views
from .views import DressList, DressDetailView





urlpatterns = [
    path('',DressList.as_view(), name='dresslist'),
    path('detail/int:<pk>/',DressDetailView.as_view(),name='detail_view'),
]
