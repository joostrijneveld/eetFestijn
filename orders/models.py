from django.db import models
from django.utils import timezone
from django.core.validators import validate_comma_separated_integer_list


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    discounts = models.ManyToManyField('Discount', blank=True)
    description = models.CharField(max_length=200, blank=True)
    _printable_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def discountstring(self):
        return ", ".join(map(str, self.discounts.all()))
    discountstring.short_description = 'Discounts'

    @property
    def printable_name(self):
        if self._printable_name:
            return self._printable_name
        return self.name

    def real_price(self, moment=None):
        discounts = [x for x in self.discounts.all() if x.is_active(moment)]
        price = self.price
        if not all(x.relative for x in discounts):
            price = min(x.value for x in discounts if not x.relative)
            price = min(price, self.price)
        return price - sum(x.value for x in discounts if x.relative)


class Order(models.Model):
    name = models.CharField(max_length=200)
    wiebetaaltwat = models.BooleanField('Via Wiebetaaltwat', default=True)
    items = models.ManyToManyField(Item, through='ItemOrder')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + ": " + ", ".join(map(str, self.items.all()))

    def itemstring(self):
        return ", ".join(map(str, self.items.all()))
    itemstring.short_description = 'Items'

    def total(self):
        return sum(x.real_price(self.date) for x in self.items.all())
    total.short_description = 'Total'

    @staticmethod
    def grandtotal():
        return sum(y.total() for y in Order.objects.all())


class ItemOrder(models.Model):
    item = models.ForeignKey(Item)
    order = models.ForeignKey(Order)

    def __str__(self):
        return str(self.item)


class Discount(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField(default=0)
    relative = models.BooleanField(default=False)
    days = models.CharField(max_length=20,
                            validators=[validate_comma_separated_integer_list])

    def __str__(self):
        return self.name

    def is_active(self, moment=None):
        if moment is None:
            moment = timezone.now()
        currentday = moment.weekday()
        return self.days and currentday in map(int, self.days.split(','))


class Category(models.Model):
    name = models.CharField(max_length=200)
    items = models.ManyToManyField(Item)
    random_item = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Receipt(models.Model):
    contents = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.contents
