form django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.models.CharField(max_length=200, blank=True, null=True)
    slug = models.models.SlugField(unique=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
    