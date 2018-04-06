from django.db import models


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
