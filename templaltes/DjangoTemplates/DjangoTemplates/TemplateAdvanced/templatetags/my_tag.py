from django import template

register = template.Library()


@register.simple_tag()
def reverse(nums):
    return nums[::-1]
