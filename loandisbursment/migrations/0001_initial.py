# Generated by Django 4.1.3 on 2022-12-26 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contributions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount_contributed', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_loaned', models.CharField(max_length=255)),
                ('expected_amount_to_be_paid', models.CharField(max_length=255)),
                ('amount_paid', models.CharField(max_length=255)),
                ('balance_carried_forward', models.CharField(max_length=255)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loandisbursment.contributions')),
            ],
        ),
    ]
