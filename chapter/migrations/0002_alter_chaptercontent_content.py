# Generated by Django 5.0.2 on 2024-05-06 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaptercontent',
            name='content',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]