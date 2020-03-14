from django import template
register = template.Library()


@register.filter
def is_private(user, file):
    return file.privates.filter(user=user).count() > 0
