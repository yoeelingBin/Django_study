# Generated by Django 3.1.7 on 2021-03-31 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='name',
            new_name='subject',
        ),
    ]
