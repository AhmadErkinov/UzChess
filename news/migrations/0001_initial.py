# Generated by Django 4.2.7 on 2023-11-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('discription', models.TextField()),
                ('posted_date', models.DateTimeField()),
                ('post_url', models.URLField(max_length=255)),
                ('image', models.FileField(blank=True, upload_to='news')),
            ],
        ),
    ]
