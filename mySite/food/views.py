from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    temlapte =loader.get_template('food/index.html')
    context={
        'item_list':item_list,
    }
    return render(context,request)

def item(request):
    return HttpResponse('this is an item view')


