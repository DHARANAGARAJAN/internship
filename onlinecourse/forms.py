from django.forms import modelForm
from .models import *

class Course_form(ModelForm)

        class Meta:

            model = Course
            fields='__all__'

class   Enrollment_form(ModelForm)

        class Meta:

                model = Enrollment
                fields='__all__'

