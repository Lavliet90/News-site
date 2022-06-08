from django import template

from news.models import CategoryArticle

register = template.Library()

@register.simple_tag()
def get_5_tags():
    return CategoryArticle.objects.all()[:5]

