from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),
]
