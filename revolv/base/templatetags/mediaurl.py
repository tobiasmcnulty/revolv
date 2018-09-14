import urlparse
from urlparse import parse_qs
from django import template
from django.conf import settings
register = template.Library()


@register.filter
def fullmediaurl(value):
    """
    TODO: determine if we really need this
    """
    # Checks for the youtube video ID in the video URL if found any and fetches the default thumbnail of the video.
    query = urlparse.urlparse(value)
    if query.hostname == 'youtu.be':
        return 'https://img.youtube.com/vi/' + query.path[1:] + '/0.jpg'

    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = parse_qs(query.query)
            return 'https://img.youtube.com/vi/' + p['v'][0] + '/0.jpg'
        if query.path[:7] == '/embed/':
            return 'https://img.youtube.com/vi/' + query.path.split('/')[2] + '/0.jpg'
        if query.path[:3] == '/v/':
            return 'https://img.youtube.com/vi/' + query.path.split('/')[2] + '/0.jpg'
    if not value.startswith('http'):
        return settings.SITE_URL + value

    return value


@register.simple_tag
def sharethis_pub_id():
    """
    return ShareThis publisher id
    """
    return settings.SHARETHIS_PUBLISHER_ID
