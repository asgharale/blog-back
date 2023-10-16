# Generated by Django 4.2.6 on 2023-10-14 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_options_rename_pub_date_post_update_and_more'),
        ('comment', '0003_rename_status_comment_confirm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='com',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post'),
        ),
    ]
