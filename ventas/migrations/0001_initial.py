# Generated by Django 5.0.1 on 2024-01-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('metric', models.FloatField()),
                ('progress', models.FloatField()),
                ('target', models.FloatField()),
                ('delta', models.FloatField()),
                ('deltaType', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'ventas',
            },
        ),
    ]
