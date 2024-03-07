# Generated by Django 5.0.2 on 2024-03-04 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('Nickname', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]