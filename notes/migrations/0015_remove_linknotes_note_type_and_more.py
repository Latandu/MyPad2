# Generated by Django 4.0.1 on 2022-01-26 19:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0014_alter_notedetails_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linknotes',
            name='note_type',
        ),
        migrations.RemoveField(
            model_name='listdetails',
            name='note_type',
        ),
        migrations.RemoveField(
            model_name='textnotes',
            name='note_type',
        ),
        migrations.AddField(
            model_name='notedetails',
            name='note_type',
            field=models.CharField(choices=[('TXN', 'Text Note'), ('LSN', 'List Note'), ('LNN', 'Link Note')], default='LSN', max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notedetails',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2022, 1, 26, 19, 36, 19, 344452, tzinfo=utc)),
        ),
    ]
