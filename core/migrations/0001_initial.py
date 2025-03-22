# Generated by Django 5.1.7 on 2025-03-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='products/')),
                ('description', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
