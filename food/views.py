from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
# Create your views here.
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request,'food/index.html',context)
def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    
    return render(request,'food/details.html',context)

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')   

    return render(request,'food/item-form.html',{'form':form})
def update_item(request,id):
    pass

def delete_item(request,id):
    pass