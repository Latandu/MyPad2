# Generated by Django 4.0.1 on 2022-01-25 22:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_remove_listnotes_note_details_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notedetails',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 25, 22, 31, 34, 774047, tzinfo=utc)),
        ),
    ]