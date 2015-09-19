# coding=utf-8
from django import template

register = template.Library()


@register.filter
def real_price_at(item, moment):
    return item.real_price(moment)
