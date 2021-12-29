from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# def categories(request):
#     return {
#         'categories' : Category.objects.all()
#     } --> refactoring

# store/home.html
def product_all(request):
    # products = Product.products.all()
    # products = Product.objects.all()
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, 'store/index.html', {'products': products})
    # return render(request, 'test.html')

#  category_list --> store/products/category.html
def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    # products = Product.objects.filter(category=category)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, 'store/category.html', {'category': category, 'products': products})

# product_detail --> store/products/category.html
def product_detail(request, slug):
    # product = get_object_or_404(Product, slug=slug, in_stock=True)
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'store/single.html', {'product': product})

    


