# Generated by Django 3.0.8 on 2020-12-31 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20201231_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domesticanimals',
            name='Income',
            field=models.TextField(),
        ),
    ]
