from django import template
from sponsorship.models import Company

register = template.Library()


@register.assignment_tag
def get_company_list(category):
    context = dict()
    context["company_list"] = Company.objects.filter(categories=category)
    return context

@register.assignment_tag
def get_sponsor_list(category):
    context = dict()
    context["sponsor_list"] = Company.objects.filter(categories=category)
    return context
