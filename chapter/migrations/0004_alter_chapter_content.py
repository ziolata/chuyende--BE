# Generated by Django 5.0.2 on 2024-05-07 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0003_chapter_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='content',
            field=models.FileField(null=True, upload_to='Content'),
        ),
    ]