# Generated by Django 4.2.6 on 2024-01-27 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sort', '0001_initial'),
        ('posts', '0006_remove_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='sort.tag'),
        ),
    ]
