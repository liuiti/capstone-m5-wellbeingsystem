# Generated by Django 4.0.6 on 2022-07-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliation',
            name='comment',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
