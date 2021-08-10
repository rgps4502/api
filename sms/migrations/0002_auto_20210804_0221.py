# Generated by Django 2.0.13 on 2021-08-04 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sms',
            old_name='album',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='sms',
            old_name='artist',
            new_name='sms',
        ),
        migrations.RenameField(
            model_name='sms',
            old_name='name',
            new_name='text',
        ),
        migrations.AddField(
            model_name='sms',
            name='timestamp',
            field=models.CharField(default=50, max_length=50),
            preserve_default=False,
        ),
    ]
