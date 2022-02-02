from statistics import mode
from django.db import models

class TopicList(models.Model):
    presentation_date = models.DateField()
    topic = models.CharField(
        max_length = 50
    )
    multi_person = models.BooleanField()
    note = models.TextField()

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ['presentation_date']
