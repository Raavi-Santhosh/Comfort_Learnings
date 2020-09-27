from courses.models import CourseCatalogue
from django import template

register = template.Library()


@register.inclusion_tag('nav_bar.html')
def nav_bar_tag():
    category = CourseCatalogue.objects.filter(is_active=True)
    return {'category': category}
