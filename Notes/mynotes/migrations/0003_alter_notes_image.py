# Generated by Django 4.1 on 2022-08-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynotes', '0002_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='notesimages'),
        ),
    ]
