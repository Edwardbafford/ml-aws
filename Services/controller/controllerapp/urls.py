from django.urls import path
from . import views

# URL to view mappings

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.flower, name='flower')
]