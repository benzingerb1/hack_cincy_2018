from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from api.resources import EntryResource, ExerciseResource

entry_resource = EntryResource()
exercise_resource = ExerciseResource()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(exercise_resource.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
