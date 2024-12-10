# Generated by Django 5.1.3 on 2024-12-10 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auction_listing_category_alter_user_id_bid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watched_by', to='auctions.auction_listing'),
        ),
    ]