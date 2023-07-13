from django.shortcuts import render
from django.views  import generic

def product_list_view(request):
    return render(request, 'products/product_list.html')

