# Generated by Django 4.0 on 2021-12-12 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appContatos', '0005_dbtabcontatos_boolexibir'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dbtabcontatos',
            name='BoolExibir',
        ),
        migrations.AddField(
            model_name='dbtabcontatos',
            name='bolExibir',
            field=models.BooleanField(default=True),
        ),
    ]
