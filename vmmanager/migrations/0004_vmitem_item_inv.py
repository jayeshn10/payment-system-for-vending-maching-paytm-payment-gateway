# Generated by Django 3.2.3 on 2021-05-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmmanager', '0003_transaction_item_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='vmitem',
            name='item_inv',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]