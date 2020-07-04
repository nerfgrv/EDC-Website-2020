from django.contrib import admin

# Register your models here.
from .models import Internship
admin.site.register(Internship)

from .models import VentureCapitalist
admin.site.register(VentureCapitalist)