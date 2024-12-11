from django import forms
from myapp.models import Appointment, ImageModel, Question


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','title','price']

    class QuestionForm(forms.ModelForm):
        class Meta:
                model = Question
                fields = ['question']