from django.contrib import admin
<<<<<<< HEAD
from . import models
# Register your models here.
admin.site.register(models.Booking)
admin.site.register(models.Language)
admin.site.register(models.Lawyer)
admin.site.register(models.Review)
admin.site.register(models.Specialities)
=======

from .models import Lawyer
# Register your models here.
admin.site.register(Lawyer)
>>>>>>> 008547b2f2393b81692bde2e18c15df630925af1
