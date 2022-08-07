from django.contrib import admin
from .models import Fish, Caught, Lure

# Register your models here.
admin.site.register(Fish)
admin.site.register(Caught)
admin.site.register(Lure)