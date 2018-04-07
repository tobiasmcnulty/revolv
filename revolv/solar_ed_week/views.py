from django.http import JsonResponse
from django.shortcuts import render
from revolv.solar_ed_week.models import HostEvent


def solar_education(request):
    return render(request, 'solar_ed_week/solar_ed_week.html')


def host_event(request):
    data = {}
    try:
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('event_title')
        date = request.POST.get('date')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        event_detail = request.POST.get('event_detail')
        facebook_link = request.POST.get('eventbrite')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        HostEvent.objects.create(
            name=name,
            email=email,
            title=title,
            date=date,
            address=address,
            city=city,
            state=state,
            zip_code=zipcode,
            detail=event_detail,
            facebook_link=facebook_link,
            latitude=latitude,
            longitude=longitude
        )
        data["success"] = True
        data["message"] = "Saved successfully"
    except Exception:
        data["success"] = False
        data["message"] = "Error while saving data"

    return JsonResponse(data)


def become_partner(request):

    name = request.POST.get('partner_name')
    email = request.POST.get('partner_email')
    organization = request.POST.get('organization')

    return render(request, '/404.html')