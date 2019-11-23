from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
      
            request.session[settings.CART_SESSION_ID] = {}

            return render(request,
                          'order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request,
                  'order_create.html',
                  {'cart': cart, 'form': form})