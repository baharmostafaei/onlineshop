from django.shortcuts import render
from django.views  import generic

from .models import Product

def home_view(request):
    return render(request, 'products/home.html')

class ProductListView(generic.ListView):

    template_name = 'products/product_list.html'
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'
    paginate_by = 15

class ProductDetailView(generic.DetailView):
    template_name = 'products/product_detail.html'
    model = Product
    context_object_name = 'product'
