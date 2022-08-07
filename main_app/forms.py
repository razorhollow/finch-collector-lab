from django.forms import ModelForm
from .models import Caught

class CaughtForm(ModelForm):
  class Meta:
    model = Caught
    fields = ['date']