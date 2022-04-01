from django.urls import path, include

from app.saludo.views import NombreListView

urlpatterns = [
    path('home/', NombreListView.as_view(), name='index'),
]
