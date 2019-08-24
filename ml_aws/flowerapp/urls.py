from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_test, name='index_test'),
    path('upload', views.flower, name='flower')
]