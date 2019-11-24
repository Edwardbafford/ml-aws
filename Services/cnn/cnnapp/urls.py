from django.urls import path
from . import views

# Url to view mapping

urlpatterns = [
    path('', views.index_test, name='index_test'),
    path('prediction/<str:image>/', views.prediction, name='prediction')
]