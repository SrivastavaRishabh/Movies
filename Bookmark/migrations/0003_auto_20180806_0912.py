# Generated by Django 2.1 on 2018-08-06 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmark', '0002_bookmarks_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmarks',
            old_name='descrption',
            new_name='description',
        ),
    ]