from django.db import models
from django.core.validators import URLValidator

class Comic(models.Model):
    comicTitle = models.CharField(max_length=500)
    comicPrice = models.CharField(max_length=500)
    comicLink = models.URLField(validators=[URLValidator()])
    comicImage = models.URLField(validators=[URLValidator()])
    def __unicode__(self):
        return unicode(self.comicTitle)
