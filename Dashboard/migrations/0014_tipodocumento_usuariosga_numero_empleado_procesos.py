# Generated by Django 5.1.2 on 2024-10-22 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0013_merge_20241021_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(max_length=20, verbose_name='')),
            ],
        ),
        migrations.AddField(
            model_name='usuariosga',
            name='numero_empleado',
            field=models.BigIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Procesos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
                ('documento', models.FileField(upload_to='filesPDF/ISO/')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.departamentos')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.empresas')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.tipodocumento')),
            ],
        ),
    ]