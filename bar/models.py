from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200)

    @models.permalink
    def get_absolute_url(self):
        return ('bar.detail', (), {'pk': self.pk})

    def __unicode__(self):
        return self.question
