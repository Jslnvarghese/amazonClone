# Generated by Django 4.1.5 on 2023-02-02 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_quantitiy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='quantitiy',
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='quantitiy',
            field=models.IntegerField(default=1),
        ),
    ]
