# Generated by Django 5.1.2 on 2024-10-19 17:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0008_alter_empresas_empresa'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoNoticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_noticia', models.CharField(max_length=20, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='FotosNoticia')),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_noticia', models.DateField(null=True)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.empresas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo_noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.tiponoticia')),
            ],
        ),
    ]