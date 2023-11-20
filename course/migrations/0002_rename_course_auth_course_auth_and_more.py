# Generated by Django 4.2.7 on 2023-11-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_auth',
            new_name='auth',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_degree',
            new_name='degree',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_lang',
            new_name='lang',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_reting',
            new_name='reting',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_sections',
            new_name='sections',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_title',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='course',
            name='like_buttom',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='more_button',
            field=models.URLField(max_length=255),
        ),
    ]
