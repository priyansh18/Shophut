from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import json
import datetime
from .utils import cartData, cookieCart, guestOrder
from .models import Product

# Create your views here.


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']

    category = request.GET.get('category', '')
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'cartItems': cartItems,
        'shipping': False,
        'current_category': category,
    }
    return render(request, 'store/store.html', context)


def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'shipping': False}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    items = data['items']
    order = data['order']

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'shipping': False}
    return render(request, 'store/checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if(action == 'add'):
        orderItem.quantity = (orderItem.quantity + 1)
    elif(action == 'remove'):
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if(orderItem.quantity <= 0):
        orderItem.delete()

    return JsonResponse("Item was Added", safe=False)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)

    else:
        customer,order=guestOrder(request,data)
       
    total = (data['form']['total'])
    order.transaction_id = transaction_id
    if total == order.get_cart_items:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode']
        )
    return JsonResponse("Payment Complete", safe=False)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'store')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'store/login.html', {'cartItems': 0})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('store')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password1)
            Customer.objects.create(user=user, name=username, email=email)
            login(request, user)
            messages.success(request, 'Account created successfully!')
            return redirect('store')

    return render(request, 'store/register.html', {'cartItems': 0})


def logout_view(request):
    logout(request)
    return redirect('store')
