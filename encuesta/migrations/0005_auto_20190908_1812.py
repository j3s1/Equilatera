# Generated by Django 2.2.5 on 2019-09-08 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0004_auto_20190908_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuestionario',
            name='respuesta',
        ),
        migrations.AddField(
            model_name='preguntas',
            name='opciones',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='respuestas',
            name='respuesta',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='encuesta.Cuestionario'),
            preserve_default=False,
        ),
    ]
