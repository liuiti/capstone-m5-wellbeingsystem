# Generated by Django 4.0.6 on 2022-07-19 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliations', '0002_alter_avaliation_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliation',
            name='comment',
            field=models.CharField(max_length=200, null=True),
        ),
    ]