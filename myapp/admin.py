from django.contrib import admin
from myapp.models import Question, Appointment, User, ImageModel

# Register your models here.

admin.site.register(Appointment)
admin.site.register(User)
admin.site.register(ImageModel)
admin.site.register(Question)

