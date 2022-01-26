# Generated by Django 4.0.1 on 2022-01-25 22:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_alter_notedetails_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listdetails',
            name='list_notes',
        ),
        migrations.AddField(
            model_name='listdetails',
            name='list_notes',
            field=models.ManyToManyField(null=True, to='notes.ListNotes'),
        ),
        migrations.AlterField(
            model_name='notedetails',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 25, 22, 36, 49, 517543, tzinfo=utc)),
        ),
    ]
