# Generated by Django 4.0.6 on 2023-06-19 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0019_bid_category_listing_auctions_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='transaction_reference',
            field=models.CharField(default='aa', max_length=100),
        ),
    ]