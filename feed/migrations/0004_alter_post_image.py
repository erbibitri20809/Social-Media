# Generated by Django 5.0.3 on 2024-07-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_remove_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
