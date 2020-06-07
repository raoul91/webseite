from django.contrib import admin
from .models import Choice, Poll, Car

admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(Car)
