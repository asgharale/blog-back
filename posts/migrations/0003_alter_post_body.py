# Generated by Django 4.2.6 on 2023-10-29 14:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_post_likes_post_liked_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]