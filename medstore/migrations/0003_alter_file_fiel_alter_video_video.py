# Generated by Django 4.2.6 on 2023-10-27 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medstore', '0002_file_fiel_video_video_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='fiel',
            field=models.FileField(upload_to='file/%Y-%m'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video/%Y-%m'),
        ),
    ]