# Generated by Django 4.0.1 on 2022-01-26 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_remove_notedetails_note_type_linknotes_note_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linknotes',
            name='note_type',
            field=models.CharField(auto_created=True, choices=[('TXN', 'Text Note'), ('LSN', 'List Note'), ('LNN', 'Link Note')], default='LNN', max_length=3),
        ),
        migrations.AlterField(
            model_name='notedetails',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 26, 9, 11, 37, 989928, tzinfo=utc)),
        ),
    ]
