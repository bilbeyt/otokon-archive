from __future__ import unicode_literals
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.dispatch import receiver


class Season(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Competition(models.Model):
    name = models.CharField(max_length=100)
    season = models.ForeignKey(Season)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Robot(models.Model):
    name = models.CharField(max_length=100)
    season = models.ForeignKey(Season)
    competition = models.ForeignKey(Competition)
    software = RichTextUploadingField()
    electronic = RichTextUploadingField()
    mechanic = RichTextUploadingField()
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name 


class RoboticsSponsors(models.Model):
    name = models.CharField(max_length=100)
    season = models.ForeignKey(Season)
    content = RichTextUploadingField()
    is_success = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class RoboticsPress(models.Model):
    name = models.CharField(max_length=100)
    season = models.ForeignKey(Season)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name


@receiver(pre_save,sender=Season)
def season_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)

@receiver(pre_save,sender=Robot)
def robot_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.name)
    
@receiver(pre_save,sender=Competition)
def competition_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.name)

@receiver(pre_save,sender=RoboticsSponsors)
def sponsors_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.name)

@receiver(pre_save,sender=RoboticsPress)
def press_slug_handler(sender,instance,*args,**kwargs):
    instance.slug = slugify(instance.name)