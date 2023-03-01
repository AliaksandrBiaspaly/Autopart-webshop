
from django.conf import settings
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from basket.basket import Basket



def order_create(request):

    basket = Basket(request)
    
    
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in basket:
                print("345")
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=(item['price']),
                                         quantity=item['qty']),
                print("123")
                product = item['product']
                product.quantity = product.quantity - item['qty']
                product.save()

        # очистка корзины
       
        basket.clear()

        return render(request, 'orders/created.html')
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html',
                  {'basket': basket, 'form': form})
