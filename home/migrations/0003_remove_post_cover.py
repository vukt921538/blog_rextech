# Generated by Django 2.2.7 on 2019-11-12 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_comment_to_comment_post_ctc_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cover',
        ),
    ]
