# coding=utf-8
from django import template

import locale

locale.setlocale(locale.LC_ALL, 'nl_NL.UTF-8')
register = template.Library()


@register.filter
def euro(cents):
    return "€ " + locale.format('%.2f', cents/100)
