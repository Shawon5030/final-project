# Generated by Django 5.1.1 on 2024-12-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_addmoney_earning_alter_addmoney_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_user', models.EmailField(max_length=254)),
                ('host_password', models.CharField(max_length=255)),
            ],
        ),
    ]
