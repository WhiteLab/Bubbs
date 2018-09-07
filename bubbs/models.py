from datetime import datetime
from django.db import models

# Create your models here.


class BidKeyGenerator(models.Model):
    year = models.IntegerField('Year', unique=True, default=int(datetime.now().strftime('%Y')))
    increment = models.IntegerField('Increment', default=0)

    class Meta:
        verbose_name = verbose_name_plural = 'BID Key Generator'

    @classmethod
    def generate(cls):
        bid_gen, _ = cls.objects.get_or_create()
        current_year = int(datetime.now().strftime('%Y'))
        if current_year != bid_gen.year:
            bid_gen.year = current_year
            bid_gen.increment = 0

        bid_gen.increment += 1
        bid_gen.save()

        bid = f'{bid_gen.year}-{bid_gen.increment}'
        Bid.objects.create(bid=bid)
        return bid


class Bid(models.Model):
    bid = models.CharField(max_length=32, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
