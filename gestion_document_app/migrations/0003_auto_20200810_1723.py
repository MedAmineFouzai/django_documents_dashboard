# Generated by Django 3.0.7 on 2020-08-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_document_app', '0002_auto_20200810_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='document_QT_QT_AT',
        ),
        migrations.AlterField(
            model_name='document',
            name='document_QT',
            field=models.IntegerField(null=True),
        ),
    ]
