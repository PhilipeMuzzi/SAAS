# Generated by Django 4.2.17 on 2024-12-10 18:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_anotacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='usuario',
        ),
        migrations.AddField(
            model_name='projeto',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='projeto',
            name='data_inicio',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='data_termino',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='projeto',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=200),
        ),
    ]
