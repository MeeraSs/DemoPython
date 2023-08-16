# Generated by Django 4.1.1 on 2023-07-18 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('contact', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]