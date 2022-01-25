from django.db import models


class NoteDetails(models.Model):
    title = models.TextField(max_length=100)
    due_date = models.DateField()
    date_created = models.DateField()