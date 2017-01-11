from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Data(models.Model):
	Familiya = models.CharField(max_length=50, null=True)
	Imya = models.CharField(max_length=50, null=True)
	Otchestvo = models.CharField(max_length=50, null=True)
	gr = models.CharField(max_length=50, null=True)
	IP = models.CharField(max_length=50, null=True)
	host = models.CharField(max_length=50, null=True)
	edit_date = models.DateField(null=True)

	def __unicode__(self):
		return self.Imya + self.Familiya

	def get_absolute_url(self):
		return reverse('data_edit', kwargs={'pk': self.pk})
