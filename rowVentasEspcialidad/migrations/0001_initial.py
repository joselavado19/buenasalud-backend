# Generated by Django 5.0.1 on 2024-01-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RowVentasEspcialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('cantidad', models.PositiveIntegerField()),
                ('especialidad', models.CharField(max_length=5)),
                ('id_especialidad', models.PositiveIntegerField()),
                ('deltaType', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'rowVentasEspcialidad',
            },
        ),
    ]
