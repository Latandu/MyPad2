from django.contrib import admin
from .models import LinkNotes, ListNotes, TextNotes, NoteDetails, ListDetails

# Register your models here.
admin.site.register(LinkNotes)
admin.site.register(ListNotes)
admin.site.register(TextNotes)
admin.site.register(NoteDetails)
admin.site.register(ListDetails)
