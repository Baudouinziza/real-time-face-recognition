# Generated by Django 3.0.4 on 2020-08-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0003_auto_20200809_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photoUrl',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
