from django.shortcuts import render
from django.http import JsonResponse
from .models import Item
from django.http import HttpResponse
import stripe
from .forms import CurrencyForm

# stripe.api_key = settings.SECRET_KEY
stripe.api_key = "sk_test_51NjdoqInrEd1EweJDGzToAhbOvSPUwbCln2gz9MnjPDed69L2j1fWQQgxXcvdiTin5C12OsmUWMY4XXy4P0F0dT700EkApx4TH"

def many(tovat):
    itog = 0
    for item in tovat:
        if item.bool:
            itog += item.price
    return convert_currency(itog, tovat[0].currency)


def convert_currency(itog, currency):
    if currency == 'usd':
        return round(itog / 90)
    elif currency == 'eur':
        return round(itog / 100)
    elif currency == 'rub':
        return round(itog * 1)
    else:
        return round(itog)

def bool_p(request,i_bool): # смена булевого значения
    tovat_bool = Item.objects.get(id=i_bool)
    if tovat_bool.bool == False:
        tovat_bool.bool = True
        tovat_bool.save()
    else:
        tovat_bool.bool = False
        tovat_bool.save()
    return index(request)

def index(request): # главная станица
    tovat = Item.objects.all()
    sum_tovar = many(tovat)
    form = select_currency(request)
    return render(request, 'api/index.html',{'tovat':tovat,'sum_tovar':sum_tovar,'form': form})

def select_currency(request): # прием и обмен валюты
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            selected_currency = form.cleaned_data['currency']
            Item.objects.update(currency=selected_currency)
            return form
    else:
        form = CurrencyForm()
    return form

def detail(request,i_det): # подробно о товара
    detail = Item.objects.filter(id=i_det)
    sum_tovar = many(detail)
    return render(request, 'api/detail.html',{'detail':detail,'sum_tovar':sum_tovar})


def buy(request, pk_id): # проверка товара перед покупкой
    if pk_id == 0:
        tov = Item.objects.filter(bool=True)
        for tovat in tov:
            buy_itog = buy_api(request,tovat)
        return buy_itog
    else:
        tovat = Item.objects.get(id=pk_id)
        buy_itog = buy_api(request,tovat)
        return buy_itog


def buy_api(request,tovat): # покупка товара
    if request.method == 'GET':
        ng = "http://localhost:8000"
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': tovat.currency,
                    'product_data': {
                        'name': tovat.name,
                    },
                    'unit_amount': int(tovat.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=ng + '/success',
            cancel_url=ng + '/cancel',
        )
        a = JsonResponse({'sessionId': session['id']})
        return a
    else:
        return HttpResponse("только GET запросы")