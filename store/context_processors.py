from category.models import Category

def categories(request):
    categories = Category.objects.filter(level=0)
    return {
        'categories': categories
    }
