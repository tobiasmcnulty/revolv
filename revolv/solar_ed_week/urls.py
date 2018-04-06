from django.conf.urls import patterns, url
from revolv.solar_ed_week.views import (solar_education)

urlpatterns = patterns(
    '',
    url(r'^', solar_education, name='solar_education'),
)
