# Generated by Django 3.2.3 on 2021-05-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_by', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]