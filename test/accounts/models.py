from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique = True)
    image = models.ImageField(upload_to='accounts/static/accounts/images', blank = True)


    def __str__(self):
        return '{0}'.format(self.name)
