# Generated by Django 2.0.2 on 2018-03-18 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0005_settle_settletransation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settletransation',
            name='penalty',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
