# myapp/api.py
from tastypie.resources import ModelResource
from api.models import Entry, Exercise

class ExerciseResource(ModelResource):
    class Meta:
        limit = 1000
        queryset = Exercise.objects.all()
        resource_name = 'exercise'