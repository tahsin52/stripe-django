from django.shortcuts import render
import stripe

from basket.basket import Basket


def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    print(total)
    total = total.replace('.', '')
    print('total:: ', total)
    total = int(total)

    stripe.api_key = ''
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid':request.user.id},
    )
    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})