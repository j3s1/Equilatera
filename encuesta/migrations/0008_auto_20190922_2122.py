# Generated by Django 2.2.5 on 2019-09-23 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0007_respuestas_pregunta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas',
            name='tipo',
            field=models.CharField(choices=[('texto', 'texto'), ('Si_No', 'Si_No'), ('Multiple', 'Multiple')], max_length=50),
        ),
    ]