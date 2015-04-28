# coding=utf-8
from django import template

import subprocess

try:
    head = subprocess.Popen("git rev-parse --short HEAD", shell=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    HEAD = head.stdout.readline().strip()
except:
    HEAD = 'unknown'

register = template.Library()


@register.simple_tag()
def git_head():
    return HEAD
