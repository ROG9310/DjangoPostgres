# Generated by Django 5.1.2 on 2024-10-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0011_merge_20241021_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventariosoporte',
            name='responsiva',
            field=models.FileField(default='', upload_to='filesPDF/Responsivas_Soporte/'),
            preserve_default=False,
        ),
    ]
