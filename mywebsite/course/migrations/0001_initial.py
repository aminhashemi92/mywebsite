# Generated by Django 3.2.6 on 2021-08-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('birthdate', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('registertime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
