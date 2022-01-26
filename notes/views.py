from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from .models import NoteDetails, ListDetails, TextNotes, LinkNotes
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter


class AllNotesViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = serializers.AllNotesSerializer
    queryset = NoteDetails.objects.all()
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['title', 'due_date', 'date_created']
    search_fields = ['textnotes__note_field', 'listnotes__list_note', 'linknotes__link_note']

    def get(self, request):
        return self.get(request)


class ListDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ListDetailsSerializer
    queryset = ListDetails.objects.all()


class TextNotesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TextNotesSerializer
    queryset = TextNotes.objects.all()


class LinkNotesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LinkNotesSerializer
    queryset = LinkNotes.objects.all()