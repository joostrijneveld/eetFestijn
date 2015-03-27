from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    discounts = models.ManyToManyField('Discount', blank=True)

    def __str__(self):
        return "{} (€ {:.2f})".format(self.name, self.price/100)


class Order(models.Model):
    name = models.CharField(max_length=200)
    in_wie_betaalt_wat = models.BooleanField('Via Wiebetaaltwat', default=True)
    items = models.ManyToManyField(Item, through='ItemOrder')

    def __str__(self):
        return self.name + ": " + ", ".join(map(str, self.items.all()))

    def itemstring(self):
        return ", ".join(map(str, self.items.all()))

    def total(self):
        return "€ {:.2f}".format(sum([x.price for x in self.items.all()])/100)

    itemstring.short_description = 'Items'
    total.short_description = 'Total'


class ItemOrder(models.Model):
    item = models.ForeignKey(Item)
    order = models.ForeignKey(Order)

    def __str__(self):
        return str(self.item)


class Discount(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField(default=0)
    relative = models.BooleanField(default=False)
    days = models.CommaSeparatedIntegerField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    items = models.ManyToManyField(Item)
