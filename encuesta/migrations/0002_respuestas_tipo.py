# Generated by Django 2.2.5 on 2019-09-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestas',
            name='tipo',
            field=models.TextField(default='text', max_length=50),
            preserve_default=False,
        ),
    ]