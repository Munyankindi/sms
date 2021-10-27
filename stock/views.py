from typing import ContextManager
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StockForm
from .models import Stock
# Stock views here.


def stock(request):
    db_objects = Stock.objects.all()
    total_stock = Stock.objects.all().count()
    
    
    if request.method == 'POST':
        form = StockForm(request.POST or None,request.FILES or None)
        if form.is_valid:
            form.save()
    form = StockForm()
    context = {
     'objectList': db_objects,
     'total': total_stock,
     'form': form,
    
    }
    return render(request,'stock/index.html',context)

    # Delete Stock
    
def delete_stock_item_view(request,pk):
    item = Stock.objects.get(id=pk)
    item.delete()
    return redirect('stock')
    
    #update Stock

def update_stock_item_view(request, pk):
    item = Stock.objects.get(id=pk)
    form = StockForm(instance=item)
 
    if request.method == 'POST':
        form = StockForm(request.POST or None,
                             request.FILES or None, instance=item)
 
        if form.is_valid():
            form.save()            
            return redirect('stock')
 
    context = {
        'form': form,
    }
    return render(request, 'stock/index.html', context)



def home(request):
    return render(request,'stock/index.html')

def contact(request):
    return render(request,'stock/index.html')
