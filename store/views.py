from django.shortcuts import render, get_object_or_404

from .models import Category, Product

def categories(request):
    return {
        'categories' : Category.objects.all()
    }

# store/home.html
def all_products(request):
    products = Product.objects.all()
    return render()

# category_list --> store/products/category.html
def category_list(request, category_slug=none):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render()

# product_detail --> store/products/category.html
def product_detail(request, slug):
    


