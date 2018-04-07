from django.conf.urls import patterns, url
from revolv.solar_ed_week.views import (solar_education, host_event)

urlpatterns = patterns(
    '',
    url(r'^event-host/$', host_event, name='host_event'),
    url(r'^', solar_education, name='solar_education'),
)
