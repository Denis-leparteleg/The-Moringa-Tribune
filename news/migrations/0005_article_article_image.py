# Generated by Django 3.2.9 on 2021-12-13 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='articles/'),
        ),
    ]
