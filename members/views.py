from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
import socket

def hello_view(request):
    name = request.GET.get('name', 'World')
    
    response_data = {
        "greeting": f"Hello, {name}"
    }
    return JsonResponse(response_data)

def info_view(request):
    
    current_time = timezone.now().isoformat()
    
    client_address = request.META.get('REMOTE_ADDR')
    
    host_name = socket.gethostname()
    
    headers = {k: v for k, v in request.META.items() if k.startswith('HTTP_')}
    
    accept_header = request.headers.get('Accept', 'N/A')
    user_agent_header = request.headers.get('User-Agent', 'N/A')
    
    response_data = {
        "time": current_time,
        "client_address": client_address,
        "host_name": host_name,
          "headers": {
            "Accept": accept_header,
            "User-Agent": user_agent_header
        }
    }
    return JsonResponse(response_data)