# Generated by Django 2.0.2 on 2018-02-20 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractBaseTransation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1023)),
                ('date', models.DateTimeField(verbose_name='Initiated Date')),
                ('initiate_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Clearing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Initiated Date')),
                ('flag_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.Bill')),
            ],
        ),
        migrations.CreateModel(
            name='BaseTransation',
            fields=[
                ('abstractbasetransation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bills.AbstractBaseTransation')),
            ],
            bases=('bills.abstractbasetransation',),
        ),
        migrations.CreateModel(
            name='BillTransation',
            fields=[
                ('abstractbasetransation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bills.AbstractBaseTransation')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.Bill')),
            ],
            bases=('bills.abstractbasetransation',),
        ),
        migrations.CreateModel(
            name='ClearingTransation',
            fields=[
                ('abstractbasetransation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bills.AbstractBaseTransation')),
                ('clearing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bills.Clearing')),
            ],
            bases=('bills.abstractbasetransation',),
        ),
        migrations.AddField(
            model_name='abstractbasetransation',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractbasetransation',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
