from django import template

register = template.Library()


@register.filter
def remainder_div(value, arg):
    try:
        if value == 0:
            return None
        return int(value) % int(arg)
    except (ValueError, ZeroDivisionError):
        return None
