# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def describe_pizzas(apps, schema_editor):
    Item = apps.get_model('orders', 'Item')

    item_descriptionpairs = (
        ("Margherita (nr. 1)", "tomaat, kaas"),
        ("Bianca (nr. 2)",  "tomaat, kaas, ui"),
        ("Napolitana (nr. 3)",  "tomaat, kaas, ansjovis"),
        ("Funghi (nr. 4)",  "tomaat, kaas, champignons"),
        ("Borromea (nr. 5)",  "tomaat, kaas, ham"),
        ("Vesuvio (nr. 6)",  "tomaat, kaas, artisjok"),
        ("Peperoni (nr. 7)",  "tomaat, kaas, paprika, spaanse peper"),
        ("Salami (nr. 8)",  "tomaat, kaas, salami"),
        ("Romagna (nr. 9)",  "tomaat, kaas, champignons, ei"),
        ("Siciliana (nr. 10)",  "tomaat, kaas, ansjovis, olijven, kappertjes"),
        ("Quatro stagioni (nr. 11)",  "tomaat, kaas, champignons, ham, salami, paprika"),
        ("Pollo (nr. 12)",  "tomaat, kaas, kip, champignons, paprika"),
        ("Capricciosa (nr. 13)",  "tomaat, kaas, champignons, ham, salami, paprika, artisjok"),
        ("Tonno (nr. 14)",  "tomaat, kaas, tonijn, ui"),
        ("Vegetaria (nr. 15)",  "tomaat, kaas, diverse groenten"),
        ("Spinazie (nr. 16)",  "met mozzarella"),
        ("Pizza shoarma (nr. 18)",  "tomaat, kaas, shoarmavlees"),
        ("Pizza döner kebab (nr. 19)",  "tomaat, kaas, dönervlees"),
        ("Estete (nr. 20)",  "ananas"),
        ("Hawaï (nr. 22)",  "ham, kaas, ananas"),
        ("Campagnola (nr. 23)",  "tomatensaus, kaas, ham, champignons, paprika en ui"),
        ("Roma (nr. 24)",  "tomatensaus, kaas, salami, champignons"),
        ("Carbonara (nr. 25)",  "tomatensaus, kaas, salami, ham en spek"),
        ("Funghi e pesce (nr. 26)",  "tomatensaus, kaas, champignons, tonijn, garnalen en mosselen"),
        ("Mafiosa (nr. 27)",  "champignons, salami, asperges, paprika, gorgonzola en parmezaanse kaas"),
        ("Santa Maria (nr. 28)",  "tomatensaus, kaas, champ, kipfilet, paprika, uien en ananas"),
        ("Paescana speciale (nr. 29)",  "tomatensaus, kaas, champignons, salami, ham, uien, spek en pikant"),
        ("Calzone vegatarisch (nr. 32)",  "verse groente"),
        ("Calzone shoarma (nr. 33)",  "gevulde pizza met kaas, shoarma"),
        ("Calzone kip (nr. 34)",  "kipfilet, champignons, paprika, ui"),
        ("Calzone fantasie (nr. 35)",  "shoarma, champignons, paprika, ui"),
        ("Calzone de Fest (nr. 36)",  "shoarma, paprika, ui, ham, salami, ananas, champignons")
    )

    for name, description in item_descriptionpairs:
        item = Item.objects.get(name=name)
        item.description = description
        item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_item_description'),
    ]

    operations = [
        migrations.RunPython(describe_pizzas)
    ]
