# Generated by Django 5.1.1 on 2024-12-26 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_youtubechannel_channel_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubechannel',
            name='statue',
            field=models.CharField(choices=[('Pending', 'Pending'), ('approved', 'approved')], default='Pending', max_length=255),
        ),
    ]
