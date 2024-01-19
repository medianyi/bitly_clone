from django.shortcuts import render, get_object_or_404, redirect

from .models import Link

# Create your views here.
from .models import Link

def index(request):
    links = Link.objects.all()
    context = {
        "links": links
    }
    return render(request, 'links/index.html', context)