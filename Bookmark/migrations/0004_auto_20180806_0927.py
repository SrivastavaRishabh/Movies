# Generated by Django 2.1 on 2018-08-06 09:27

from django.db import migrations
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Bookmark', '0003_auto_20180806_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmarks',
            name='tags',
        ),
        migrations.AddField(
            model_name='bookmarks',
            name='tags',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
    ]
