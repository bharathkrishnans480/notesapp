# Generated by Django 4.1 on 2022-08-19 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mynotes', '0006_rename_description_notes_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='content',
            new_name='description',
        ),
    ]
