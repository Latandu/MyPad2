from rest_framework import serializers

from .models import NoteDetails, ListNotes, ListDetails, TextNotes, LinkNotes


class AllNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteDetails
        fields = '__all__'


class TextNotesSerializer(serializers.ModelSerializer):
    note_details = AllNotesSerializer()

    class Meta:
        model = TextNotes
        fields = '__all__'

    # explicit method for creating writable nested serializers
    def create(self, validated_data):
        note_details = validated_data.pop('note_details')
        note_details_create = NoteDetails.objects.create(**note_details)
        print(note_details_create)
        text_note = TextNotes.objects.create(note_details=note_details_create, **validated_data)
        return text_note

    def update(self, instance, validated_data):
        note_details_data = validated_data.pop('note_details')
        note_details = instance.note_details

        note_details.save()
        instance.note_field = validated_data.get('note_field', instance.note_field)
        validated_data.note_type = validated_data.get('note_type', instance.note_type)
        instance.save()
        return instance


class ListNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListNotes
        fields = '__all__'


class ListDetailsSerializer(serializers.ModelSerializer):
    note_details = AllNotesSerializer()
    list_notes = ListNotesSerializer(many=True)

    class Meta:
        model = ListDetails
        fields = '__all__'

    def create(self, validated_data):
        note_details = validated_data.pop('note_details')
        note_details_create = NoteDetails.objects.create(**note_details)
        list_notes = validated_data.pop('list_notes')
        list_notes_create = ListNotes.objects.create(**list_notes)
        list_details = ListDetails.objects.create(note_details=note_details_create, list_notes=list_notes_create)
        return list_details


class LinkNotesSerializer(serializers.ModelSerializer):
    note_details = AllNotesSerializer()

    class Meta:
        model = LinkNotes
        fields = '__all__'

    def create(self, validated_data):
        note_details = validated_data.pop('note_details')
        note_details_create = NoteDetails.objects.create(**note_details)
        link_note = LinkNotes.objects.create(note_details=note_details_create, **validated_data)
        return link_note
