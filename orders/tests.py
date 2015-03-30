# coding=utf-8
from django.test import TestCase
from orders.models import Item, Order, ItemOrder, Discount
import datetime

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="Knakworst", price=210)
        Item.objects.create(name="Friet zonder (klein)", price=160)
        Item.objects.create(name="extra ras/aardappel", price=25)

    def test_real_price(self):
        knakworst = Item.objects.get(name="Knakworst")
        friet = Item.objects.get(name="Friet zonder (klein)")
        aardappel = Item.objects.get(name="extra ras/aardappel")
        self.assertEqual(knakworst.real_price, 210)
        self.assertEqual(friet.real_price, 160)
        self.assertEqual(aardappel.real_price, 25)


class OrderTestCase(TestCase):
    def setUp(self):
        Order.objects.create(name="Testname1")
        Order.objects.create(name="Testname2")
        knakworst = Item.objects.create(name="Knakworst", price=210)
        friet = Item.objects.create(name="Friet zonder (klein)", price=160)
        aardappel = Item.objects.create(name="extra ras/aardappel", price=25)
        self.items = [knakworst, friet, aardappel]

    def test_duplicates(self):
        order = Order.objects.get(name="Testname1")
        ItemOrder.objects.create(item=self.items[0], order=order)
        ItemOrder.objects.create(item=self.items[0], order=order)
        order.save()
        self.assertEqual(order.total(), 420)
        self.assertEqual(len(order.items.all()), 2)

    def test_total(self):
        order = Order.objects.get(name="Testname1")
        for item in self.items:
            ItemOrder.objects.create(item=item, order=order)
        order.save()
        self.assertEqual(order.total(), 395)

    def test_grandtotal(self):
        order1 = Order.objects.get(name="Testname1")
        order2 = Order.objects.get(name="Testname2")
        for item in self.items:
            ItemOrder.objects.create(item=item, order=order1)
            ItemOrder.objects.create(item=item, order=order2)
        order1.save()
        order2.save()
        self.assertEqual(Order.grandtotal(), 790)


class DiscountTestCase(TestCase):
    def test_relative_discount(self):
        schoteldag = Discount.objects.create(
            name="Schoteldag", days=str(datetime.datetime.today().weekday()),
            relative=True, value=200)
        item = Item.objects.create(name="Satéschotel", price=800)
        item.discounts.add(schoteldag)
        self.assertEqual(item.real_price, 600)

    def test_absolute_discount(self):
        pizzadag25 = Discount.objects.create(
            name="Pizzadag (t/m 25)", relative=False, value=600,
            days=str(datetime.datetime.today().weekday()))
        item = Item.objects.create(name="Siciliana", price=800)
        item.discounts.add(pizzadag25)
        self.assertEqual(item.real_price, 600)

    def test_absolute_cheaper(self):
        pizzadag25 = Discount.objects.create(
            name="Pizzadag (t/m 25)", relative=False, value=600,
            days=str(datetime.datetime.today().weekday()))
        item = Item.objects.create(name="Margherita", price=500)
        item.discounts.add(pizzadag25)
        self.assertEqual(item.real_price, 500)

    def test_active(self):
        pizzadag25 = Discount.objects.create(
            name="Pizzadag (t/m 25)", relative=False, value=600,
            days=str(datetime.datetime.today().weekday()))
        self.assertTrue(pizzadag25.is_active())

    def test_inactive(self):
        pizzadag25 = Discount.objects.create(
            name="Pizzadag (t/m 25)", relative=False, value=600,
            days='')
        self.assertFalse(pizzadag25.is_active())
