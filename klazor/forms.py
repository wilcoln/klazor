from django.forms import ModelForm
from klazor.models import *


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'tag_set', 'instructor_set', 'year']
