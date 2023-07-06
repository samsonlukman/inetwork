# Generated by Django 4.1.7 on 2023-07-02 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0023_remove_listing_image_listingimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('transaction_reference', models.CharField(default='aa', max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('isActive', models.BooleanField(default=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MarketCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MarketCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currencyName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MarketImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='network.market')),
            ],
        ),
        migrations.CreateModel(
            name='MarketComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='market_userComment', to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marketComment', to='network.market')),
            ],
        ),
        migrations.AddField(
            model_name='market',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='market_category', to='network.marketcategory'),
        ),
        migrations.AddField(
            model_name='market',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='market_currency', to='network.marketcurrency'),
        ),
        migrations.AddField(
            model_name='market',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='market_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='market',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='market_watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]