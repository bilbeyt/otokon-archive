from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Organization(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    active = models.BooleanField(default=False)
    order = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization)
    sponsorship = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Company(models.Model):
    name = models.CharField(max_length=200)
    content = RichTextField()
    organization = models.ForeignKey(Organization)
    categories = models.ManyToManyField(Category)
    created=models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200)
    success = models.BooleanField("Is meeting successfull ?", default=False)
    meeting = models.BooleanField("Is this company called?", default=False)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Category)
def category_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)

@receiver(pre_save, sender=Company)
def company_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)

@receiver(pre_save, sender=Organization)
def organization_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
