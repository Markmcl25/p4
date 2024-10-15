from django.shortcuts import render
from .models import Item
from django.http import HttpResponse

# Create your views here.

# View to list all items
def item_list(request):
    items = Item.objects.all()  # Fetch all items from the database
    return render(request, 'inventory/item_list.html', {'items': items})