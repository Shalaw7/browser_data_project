from django.shortcuts import render

from django.shortcuts import redirect
from django.http import JsonResponse
from .models import BrowserData

def collect_data(request):
    # Collect basic data
    ip_address = get_client_ip(request)
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    
    # Save data to the database
    BrowserData.objects.create(
        ip_address=ip_address,
        user_agent=user_agent,
        screen_resolution=request.GET.get('resolution', 'Unknown'),
        device_type=request.GET.get('device', 'Unknown'),
        os=request.GET.get('os', 'Unknown'),
    )
    
    # Redirect the user to the target site
    return redirect('https://maps.app.goo.gl/6XgLdHw8eBFHTSheA')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
