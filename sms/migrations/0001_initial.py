# Generated by Django 2.0.13 on 2021-08-02 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=50)),
                ('album', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
