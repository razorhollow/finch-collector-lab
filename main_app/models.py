from django.db import models
# anadromous, saltwater, freshwater

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
  picture = models.URLField(default="")

  def __str__(self):
    return self.name