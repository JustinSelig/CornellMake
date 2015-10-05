from django.shortcuts import render
from django.db.models import Q

# Create your views here.

def media(request):
    return render(request, 'media.html')
    
def search(request):
    type_filter = Q()
    
