from .models import Category

# Pindahan dari view
def categories(request):
    return {
        'categories': Category.objects.all()
    }