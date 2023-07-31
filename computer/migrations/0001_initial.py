# Generated by Django 4.2.3 on 2023-07-26 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerBrands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='Media')),
            ],
        ),
        migrations.CreateModel(
            name='ComputerGeneration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ComputerSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generation', models.CharField(max_length=50)),
                ('price_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_max', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ram', models.PositiveIntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='computer.computerbrands')),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_code', models.CharField(max_length=50, unique=True)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_rate', models.PositiveIntegerField()),
                ('total_price', models.PositiveIntegerField()),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='computer', to='computer.computergeneration')),
            ],
        ),
    ]