# myapp/api.py
from tastypie.resources import ModelResource
from api.models import Entry, Exercise


class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'

class ExerciseResource(ModelResource):
    class Meta:
        queryset = Exercise.objects.all()
        resource_name = 'exercise'