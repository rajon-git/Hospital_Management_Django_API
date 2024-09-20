from django.contrib import admin
from .models import Designation, Specialization, AvailableTime,Doctor

# Register your models here.
admin.site.register(Specialization)
admin.site.register(Designation)
admin.site.register(AvailableTime)
admin.site.register(Doctor)
