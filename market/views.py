from django.shortcuts import render
from .models import Deals
from django.utils import timezone

def deals_list(request):
    deals = Deals.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'market/deal_list.html', context={'deals': deals})

def main(request):
    return render(request, 'market/main.html', {})
# Create your views here.
