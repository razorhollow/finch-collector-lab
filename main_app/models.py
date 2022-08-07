from django.db import models
from django.urls import reverse 

CATEGORIES = (
  ('F', 'Freshwater'),
  ('S', 'Saltwater'),
  ('A', 'Anadromous')
)

# Create your models here.
class Fish(models.Model):
  name = models.CharField(max_length=100, default='fish')
  scientific_name = models.CharField(max_length=100, default="")
  category = models.CharField(
    max_length=1,
    choices=CATEGORIES,
    default=CATEGORIES[0][0]
  )
  picture = models.URLField(blank=True, default="")

  def __str__(self):
    return self.name

class Caught(models.Model):
  date = models.DateField('Catch Date')
  fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

  def __str__(self):
    return f"Caught on {self.date}"

  class Meta:
    ordering = ['-date']

class Lure(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=30)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('lure_detail', kwargs={'pk': self.id})