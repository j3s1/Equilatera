# Generated by Django 2.2.5 on 2019-09-30 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0011_auto_20190929_2121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizaciones',
            old_name='razon',
            new_name='nombre',
        ),
    ]