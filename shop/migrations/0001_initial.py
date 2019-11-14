# Generated by Django 2.2.7 on 2019-11-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, upload_to='product')),
                ('description', models.TextField()),
                ('hard_ware', models.TextField()),
            ],
        ),
    ]
