from django.db import models

class Poll(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.slug)


class Choice(models.Model):
    poll = models.ForeignKey(to='Poll', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}: {1}".format( self.poll.name , self.name )

class Car(models.Model):
    name = models.CharField(max_length = 64)
    ps = models.IntegerField(default = 0)
    brand = models.CharField(max_length = 64)

    def __str__(self):
        return "{0}".format(self.name)
