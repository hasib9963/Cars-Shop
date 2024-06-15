from django.urls import path
from . import views
urlpatterns = [

    path('add/', views.AddCarCreateView.as_view(), name='add_car'),
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car'),
]
