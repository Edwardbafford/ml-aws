from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('flower/', include('flowerapp.urls')),
    path('admin/', admin.site.urls),
]
