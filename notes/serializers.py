from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import NoteDetails, ListNotes, ListDetails, TextNotes, LinkNotes


class AllNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteDetails
        fields = '__all__'


class TextNotesSerializer(WritableNestedModelSerializer):
    note_details = AllNotesSerializer()

    class Meta:
        model = TextNotes
        fields = '__all__'


class ListNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListNotes
        fields = '__all__'


class ListDetailsSerializer(WritableNestedModelSerializer):
    note_details = AllNotesSerializer()
    list_notes = ListNotesSerializer(many=True)

    class Meta:
        model = ListDetails
        fields = '__all__'


class LinkNotesSerializer(WritableNestedModelSerializer):
    note_details = AllNotesSerializer()

    class Meta:
        model = LinkNotes
        fields = '__all__'