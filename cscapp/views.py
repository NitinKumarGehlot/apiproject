from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
def handle_page_not_found(request,exception):
    return render(request,'cscapp/404.html')

def handle_server_error(request):
    return render(request,'cscapp/500.html')

def handle_permission_denied(request, exception):
    return render(request,'cscapp/403.html')

def handle_bad_request(request, exception):
    return render(request,'cscapp/400.html')