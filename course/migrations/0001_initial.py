# Generated by Django 4.2.7 on 2023-11-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=255)),
                ('course_auth', models.CharField(max_length=255)),
                ('course_price', models.CharField(max_length=255)),
                ('course_reting', models.DecimalField(decimal_places=2, max_digits=4)),
                ('course_lang', models.CharField(max_length=8)),
                ('course_sections', models.CharField(max_length=255)),
                ('course_degree', models.CharField(max_length=255)),
                ('course_category', models.CharField(max_length=255)),
                ('course_image', models.FileField(blank=True, upload_to='course/')),
                ('more_button', models.URLField()),
                ('like_buttom', models.FileField(blank=True, upload_to='course/')),
            ],
        ),
    ]
