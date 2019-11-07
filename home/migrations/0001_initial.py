# Generated by Django 2.2.6 on 2019-11-04 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=30)),
                ('dob', models.DateField(null=True)),
                ('f_name', models.CharField(max_length=10)),
                ('l_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('descriptions', models.TextField()),
                ('img', models.ImageField(blank=True, default='avata/178697.png', upload_to='avata')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_published', models.DateTimeField(auto_now=True)),
                ('cover', models.ImageField(blank=True, default='cover/cover_default.jpg', upload_to='cover')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_box', models.TextField()),
                ('comment_time', models.DateTimeField(auto_now=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_to_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_field', models.TextField()),
                ('comment_ctc_time', models.DateTimeField(auto_now=True)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.CommentPost')),
                ('post_ctc_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.Post')),
                ('user_ctc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile')),
            ],
        ),
    ]
