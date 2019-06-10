# Generated by Django 2.2.2 on 2019-06-10 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_series', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Processors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_count', models.IntegerField()),
                ('thread_count', models.IntegerField()),
                ('tdp_watts', models.IntegerField()),
                ('model_name', models.CharField(max_length=255)),
                ('rrp_usd', models.DecimalField(decimal_places=2, max_digits=10)),
                ('base_clock', models.DecimalField(decimal_places=2, max_digits=10)),
                ('turbo_clock', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processors.Manufacturer')),
                ('model_series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processors.ProductSeries')),
            ],
        ),
    ]
