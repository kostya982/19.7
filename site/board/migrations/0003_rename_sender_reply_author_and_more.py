# Generated by Django 4.2.5 on 2023-10-03 15:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_remove_reply_receiver_alter_post_post_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='sender',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='reply',
            old_name='feedback',
            new_name='content',
        ),
        migrations.AddField(
            model_name='reply',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='board.post'),
        ),
    ]
