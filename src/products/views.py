from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import Product

# Creates a list of all products in the database
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

# Renders the list of products
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

# Renders the list of individual product details
def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk) # product id
    instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
