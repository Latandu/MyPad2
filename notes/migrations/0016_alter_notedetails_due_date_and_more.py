# Generated by Django 4.0.1 on 2022-01-26 19:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0015_remove_linknotes_note_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notedetails',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 26, 19, 40, 5, 913654, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='notedetails',
            name='note_type',
            field=models.CharField(choices=[('TXN', 'Text Note'), ('LSN', 'List Note'), ('LNN', 'Link Note')], editable=False, max_length=3),
        ),
    ]
