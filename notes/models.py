import datetime

from django.utils import timezone

from django.db import models

NOTE_TYPE_CHOICES = [
    ('TXN', "Text Note"),
    ('LSN', "List Note"),
    ('LNN', "Link Note"),
]


class NoteDetails(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField(default=datetime.date.today)
    date_created = models.DateField(auto_now=True)
    note_type = models.CharField(max_length=3, choices=NOTE_TYPE_CHOICES, editable=False)

    def __str__(self):
        return self.title


class TextNotes(models.Model):
    note_details = models.OneToOneField(NoteDetails, on_delete=models.CASCADE)
    note_field = models.TextField(max_length=500)

    def __str__(self):
        return self.note_field


class ListNotes(models.Model):
    list_note = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)


class ListDetails(models.Model):
    note_details = models.ForeignKey(NoteDetails, on_delete=models.CASCADE)
    list_notes = models.ManyToManyField(ListNotes, null=True)


class LinkNotes(models.Model):
    note_details = models.OneToOneField(NoteDetails, on_delete=models.CASCADE)
    link_note = models.URLField()

    def __str__(self):
        return self.link_note
