# Generated by Django 4.2.17 on 2024-12-11 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_projeto_membros'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacao',
            name='convite',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.convite'),
        ),
    ]
