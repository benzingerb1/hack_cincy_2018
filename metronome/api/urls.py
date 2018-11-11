from django.urls import path
from django.conf.urls import include
from api.resources import ExerciseResource

exercise_resource = ExerciseResource()

urlpatterns = [
    path('', include(exercise_resource.urls)),
]