# Generated by Django 3.0.4 on 2020-08-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reason',
            field=models.CharField(max_length=200),
        ),
    ]
