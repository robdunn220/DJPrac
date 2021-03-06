from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

# Create your views here.
from .models import Product

# Creates a list of all products in the database
class ProductListView(ListView):
    template_name = 'products/list.html'
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

# List view of all products with featured
class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

# List view of selected product with featured
class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/featured-detail.html"
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()

# Renders the list of products
def product_list_view(request):
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)

# Generates specific product URL and view based on SLUG tag
class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Nope")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Merp")
        return instance

# Renders the list of individual product details
class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Non-existent product")
        return instance


# Renders the list of individual product details
def product_detail_view(request, pk=None, *args, **kwargs):
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Non-existent product")
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
