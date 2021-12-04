from django.shortcuts import render

# Create your views here.
def account_list(request):
    # basket = Basket(request)
    return render(request, 'store/account/account.html')