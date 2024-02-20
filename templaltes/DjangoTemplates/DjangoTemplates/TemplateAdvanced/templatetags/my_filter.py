from django import template

register = template.Library()


@register.filter(name='odd')
def odd(nums):
    return [x for x in nums if x % 2 != 0]
