# Generated by Django 3.0.8 on 2020-12-09 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_auto_20201209_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='Business',
            field=models.CharField(max_length=110, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='Intrest',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='Jobs',
            field=models.CharField(max_length=110, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='News_Paper',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
