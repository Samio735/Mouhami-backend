from django.contrib import admin

# Register your models here.
from .models import Lawyer,Language,Specialities
# Register your models here.
admin.site.register(Specialities)

admin.site.register(Lawyer)

admin.site.register(Language)
