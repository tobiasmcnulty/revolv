from django.shortcuts import render


def solar_education(request):
    return render(request, 'solar_ed_week/solar_ed_week.html')