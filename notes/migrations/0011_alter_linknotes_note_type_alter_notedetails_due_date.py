# Generated by Django 4.0.1 on 2022-01-26 09:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_alter_linknotes_note_type_alter_notedetails_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linknotes',
            name='note_type',
            field=models.CharField(choices=[('TXN', 'Text Note'), ('LSN', 'List Note'), ('LNN', 'Link Note')], default='LNN', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='notedetails',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 26, 9, 17, 10, 339030, tzinfo=utc)),
        ),
    ]