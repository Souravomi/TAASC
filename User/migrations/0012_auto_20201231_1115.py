# Generated by Django 3.0.8 on 2020-12-31 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_auto_20201231_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='Income',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='fish',
            name='Land_Area',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='rubber',
            name='Income',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vegfru',
            name='Income',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vegfru',
            name='Land_Area',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vegfru',
            name='Marketing',
            field=models.CharField(max_length=25),
        ),
    ]
