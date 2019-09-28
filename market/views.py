from django.shortcuts import render, render_to_response
from .models import Deals
from django.utils import timezone
from django.views.generic import TemplateView


def deals_list(request):
    deals = Deals.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'market/deal_list.html', context={'deals': deals})

def main(request):
    return render(request, 'market/main.html', {})
# Create your views here.

def sign_in(request):
    return render(request, 'market/authorization.html', {})

def get_stats(request):
    data = Deals.objects.all()
    return render(request,'market/stats.html',{'data':data})


class HomeView(TemplateView):
    template_name = "market/home.html"

def table(request):
     datatable = Deals.objects.all()
     return render(request, 'market/tables.html', {'datatable':datatable})