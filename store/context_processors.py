from .models import Category


# Pindahan dari view
def categories(request):
    return {
        # 'categories': Category.objects.all()
        'categories': Category.objects.filter(level=0)
    }