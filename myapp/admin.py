from django.contrib import admin
from myapp.models import Member, Product, Appointment, User, ImageModel

# Register your models here.
admin.site.register(Member)
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(User)
admin.site.register(ImageModel)

