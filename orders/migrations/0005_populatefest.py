# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def populate_fest(apps, schema_editor):
    """This function seeds the database with the menu of the Fest as it was
    on 2015-04-10
    """

    Discount = apps.get_model("orders", "Discount")
    Item = apps.get_model("orders", "Item")

    schoteldag = Discount.objects.create(
        name="Schoteldag", days='2,3', relative=True, value=200)
    pizzadag25 = Discount.objects.create(
        name="Pizzadag (t/m 25)", days='0,1', relative=False, value=600)
    pizzadag2635 = Discount.objects.create(
        name="Pizzadag (26 t/m 35)", days='0,1', relative=False, value=800)

    def add_item(name, price, *discounts):
        item = Item.objects.create(name=name, price=price)
        if discounts:
            for discount in discounts:
                item.discounts.add(discount)

    add_item("Friet zonder (klein)", 160)
    add_item("Friet zonder (groot)", 210)
    add_item("Friet mayonaise (klein)", 200)
    add_item("Friet mayonaise (groot)", 230)
    add_item("Friet speciaal (klein)", 220)
    add_item("Friet speciaal (groot)", 270)
    add_item("Friet saté (klein)", 220)
    add_item("Friet saté (groot)", 270)
    add_item("Friet oorlog (klein)", 240)
    add_item("Friet oorlog (groot)", 290)
    add_item("Friet stoofvlees (klein)", 300)
    add_item("Friet stoofvlees (groot)", 350)
    add_item("Friet super (klein)", 375)
    add_item("Friet super (groot)", 425)
    add_item("Friet super saté (klein)", 375)
    add_item("Friet super saté (groot)", 425)
    add_item("Friet super oorlog (klein)", 400)
    add_item("Friet super oorlog (groot)", 450)
    add_item("Friet waterfiets (klein)", 450)
    add_item("Friet waterfiets (groot)", 500)
    add_item("Friet knoflook (klein)", 220)
    add_item("Friet knoflook (groot)", 270)
    add_item("Friet joppie (klein)", 220)
    add_item("Friet joppie (groot)", 270)
    add_item("Gezinszak friet", 500)
    add_item("extra ras/aardappel", 25)

    add_item("Frikandel", 150)
    add_item("Frikandel speciaal", 190)
    add_item("Kroket", 150)
    add_item("Goulash kroket", 160)
    add_item("Satékroket", 160)
    add_item("Bamischijf", 160)
    add_item("Nasischijf", 160)
    add_item("Gehaktbal", 200)
    add_item("Kwekkerboom", 180)
    add_item("Pikanto", 210)
    add_item("Kipcorn", 190)
    add_item("Mexicano", 210)
    add_item("Lihanboutje", 160)
    add_item("Bitterballen (10st)", 250)
    add_item("Viandel", 210)
    add_item("Braadworst", 210)
    add_item("Knakworst", 210)
    add_item("Sitostick", 210)
    add_item("Visstick", 220)
    add_item("Berenklauw", 220)
    add_item("Smulrol", 220)
    add_item("Shoarmarol", 220)
    add_item("Loempia klein", 160)
    add_item("Loempia groot", 275)
    add_item("Vlammetjes (6st)", 250)
    add_item("Kipnuggets (6st)", 250)
    add_item("Mini nasi (6st)", 250)
    add_item("Mini bami (6st)", 250)
    add_item("Nasi vegetarisch", 190)
    add_item("Bami vegetarisch", 190)
    add_item("Cheese crack", 190)
    add_item("Kaassoufflé", 160)

    add_item("Dürüm döner", 500)
    add_item("Dürüm shoarma", 500)
    add_item("Dürüm kip döner", 500)

    add_item("Rundvleessalade", 200)
    add_item("Gemengde salade", 200)
    add_item("Salade de Fest", 600)
    add_item("Salade tonno", 500)

    add_item("Broodje kroket", 200)
    add_item("Broodje frikandel", 200)
    add_item("Broodje viandel", 250)
    add_item("Broodje kipkorn", 230)
    add_item("Broodje gehaktbal", 250)
    add_item("Broodje braadworst", 260)
    add_item("Broodje knakworst", 260)
    add_item("Broodje pikanto", 260)
    add_item("Broodje mexicano", 260)
    add_item("Broodje visstick", 270)
    add_item("Broodje goulashkroket", 210)
    add_item("Broodje satékroket", 210)
    add_item("Broodje ham", 200)
    add_item("Broodje ham en kaas", 250)

    add_item("Portie satéstokjes", 450)
    add_item("Satéschotel", 800, schoteldag)

    add_item("Halve haan", 500)
    add_item("Halve-haan-schotel", 900, schoteldag)

    add_item("Broodje hamburger speciaal", 300)
    add_item("Broodje hamburger Hawaï", 400)
    add_item("Hamburgerschotel", 850, schoteldag)
    add_item("Hamburgerschotel Hawaï", 900, schoteldag)

    add_item("Broodje kipfilet", 600)
    add_item("Broodje kip groot", 800)
    add_item("Friet kip", 800)
    add_item("Kipschotel", 1000, schoteldag)

    add_item("Broodje shoarma", 500)
    add_item("Broodje shoarma fantasie", 600)
    add_item("Broodje shoarma groot", 700)
    add_item("Broodje shoarma ananas", 600)
    add_item("Broodje shoarma kaas", 600)
    add_item("Friet shoarma", 700)
    add_item("Friet shoarma kaas", 800)
    add_item("Shoarmaschotel", 900, schoteldag)
    add_item("Shoarmaschotel fantasie", 1000, schoteldag)
    add_item("Shoarmaschotel ananas", 1000, schoteldag)

    add_item("Broodje döner", 500)
    add_item("Broodje döner fantasie", 600)
    add_item("Broodje döner groot", 700)
    add_item("Friet döner", 700)
    add_item("Dönerschotel", 900, schoteldag)
    add_item("Dönerschotel fantasie", 1000, schoteldag)

    add_item("Broodje kipdöner", 500)
    add_item("Broodje kipdöner fantasie", 600)
    add_item("Broodje kipdöner ananas", 600)
    add_item("Friet kipdöner", 700)
    add_item("Kipdönerschotel", 900, schoteldag)
    add_item("Kipdönerschotel fantasie", 1000, schoteldag)
    add_item("Kipdönerschotel ananas", 1000, schoteldag)

    add_item("Lahmacun met groente", 300)
    add_item("Lahmacun met döner", 500)
    add_item("Lahmacun met shoarma", 500)
    add_item("Lahmacun met kipdöner", 500)

    add_item("Kapsalon vegetarisch (klein)", 650)
    add_item("Kapsalon vegetarisch (groot)", 850)
    add_item("Kapsalon döner (klein)", 650)
    add_item("Kapsalon döner (groot)", 850)
    add_item("Kapsalon shoarma (klein)", 650)
    add_item("Kapsalon shoarma (groot)", 850)
    add_item("Kapsalon kipdöner (klein)", 650)
    add_item("Kapsalon kipdöner (groot)", 850)
    add_item("Kapsalon kipfilet (klein)", 650)
    add_item("Kapsalon kipfilet (groot)", 850)

    add_item("Spareribsschotel", 1200, schoteldag)

    add_item("Kaassouffléschotel", 700, schoteldag)
    add_item("Kroketschotel", 750, schoteldag)
    add_item("Frikandelschotel", 750, schoteldag)
    add_item("Pikantoschotel", 850, schoteldag)
    add_item("Mexicanoschotel", 850, schoteldag)
    add_item("Kipcornschotel", 850, schoteldag)

    add_item("Shoarma-/dönerschotel", 1100, schoteldag)
    add_item("Shoarma-/kipdönerschotel", 1100, schoteldag)
    add_item("Shoarma-/kipfiletschotel", 1100, schoteldag)

    add_item("Schnitzelschotel", 800, schoteldag)
    add_item("Schnitzel champignons", 1000, schoteldag)
    add_item("Schnitzel zigeunersaus", 900, schoteldag)

    add_item("Margherita (nr. 1)", 500, pizzadag25)
    add_item("Bianca (nr. 2)", 600, pizzadag25)
    add_item("Napolitana (nr. 3)", 650, pizzadag25)
    add_item("Funghi (nr. 4)", 650, pizzadag25)
    add_item("Borromea (nr. 5)", 650, pizzadag25)
    add_item("Vesuvio (nr. 6)", 650, pizzadag25)
    add_item("Peperoni (nr. 7)", 650, pizzadag25)
    add_item("Salami (nr. 8)", 650, pizzadag25)
    add_item("Romagna (nr. 9)", 700, pizzadag25)
    add_item("Siciliana (nr. 10)", 800, pizzadag25)
    add_item("Quatro stagioni (nr. 11)", 900, pizzadag25)
    add_item("Pollo (nr. 12)", 900, pizzadag25)
    add_item("Capricciosa (nr. 13)", 900, pizzadag25)
    add_item("Tonno (nr. 14)", 850, pizzadag25)
    add_item("Vegetaria (nr. 15)", 900, pizzadag25)
    add_item("Spinazie (nr. 16)", 900, pizzadag25)
    add_item("Pizza döner speciaal (nr. 17)", 950, pizzadag25)
    add_item("Pizza shoarma speciaal (nr. 17)", 950, pizzadag25)
    add_item("Pizza shoarma (nr. 18)", 900, pizzadag25)
    add_item("Pizza döner kebab (nr. 19)", 900, pizzadag25)
    add_item("Estete (nr. 20)", 700, pizzadag25)
    add_item("Gorgonzola al fromaggio (nr. 21)", 900, pizzadag25)
    add_item("Hawaï (nr. 22)", 900, pizzadag25)
    add_item("Campagnola (nr. 23)", 850, pizzadag25)
    add_item("Roma (nr. 24)", 800, pizzadag25)
    add_item("Carbonara (nr. 25)", 900, pizzadag25)

    add_item("Funghi e pesce (nr. 26)", 1100, pizzadag2635)
    add_item("Mafiosa (nr. 27)", 1000, pizzadag2635)
    add_item("Santa Maria (nr. 28)", 1000, pizzadag2635)
    add_item("Paescana speciale (nr. 29)", 1000, pizzadag2635)
    add_item("Marinara (nr. 30)", 1000, pizzadag2635)
    add_item("Pizza De Fest speciaal (nr. 31)", 1100, pizzadag2635)
    add_item("Calzone vegatarisch (nr. 32)", 950, pizzadag2635)
    add_item("Calzone shoarma (nr. 33)", 1000, pizzadag2635)
    add_item("Calzone kip (nr. 34)", 1000, pizzadag2635)
    add_item("Calzone fantasie (nr. 35)", 1000, pizzadag2635)
    add_item("Calzone de Fest (nr. 36)", 1100, pizzadag2635)
    add_item("-extra vlees", 200)
    add_item("-extra groente of fruit", 50)
    add_item("-extra ham of salami", 100)

    add_item("Knoflooksaus", 75)
    add_item("Mayonaise", 75)
    add_item("Sambalsaus", 75)
    add_item("Tomatensaus", 75)
    add_item("Cocktailsaus", 75)
    add_item("Joppiesaus", 100)
    add_item("Currysaus", 100)
    add_item("Satésaus (klein)", 125)
    add_item("Satésaus (groot)", 250)


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20150328_0929'),
    ]

    operations = [
        migrations.RunPython(populate_fest)
    ]
