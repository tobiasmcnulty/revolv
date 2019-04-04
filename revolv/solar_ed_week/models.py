from django.db import models
from django.db.models import ImageField


class HostEvent(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    detail = models.TextField()
    facebook_link = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=17,
        decimal_places=14,
        default=0.0
    )
    longitude = models.DecimalField(
        max_digits=17,
        decimal_places=14,
        default=0.0
    )
    evntime = models.TimeField(null=True)


class BecomePartner(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    promote_solar = models.BooleanField(default=False)
    promoting_way = models.TextField()
    logo = ImageField(
        upload_to='become_partner/',
        blank=True,
        null=True
    )


class BecomeSponsor(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    financially_support = models.BooleanField(default=False)
    logo = ImageField(
        upload_to='become_sponsor/',
        blank=True,
        null=True
    )
