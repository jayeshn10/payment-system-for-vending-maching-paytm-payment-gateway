# Generated by Django 3.2.3 on 2021-05-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmmanager', '0004_vmitem_item_inv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='made_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]