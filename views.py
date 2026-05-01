from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Buyer, Camera, CartItem


def catalog(request):
    cameras = Camera.objects.all()
    return render(request, 'catalog.html', {'cameras': cameras})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if Buyer.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким логином уже существует')
        else:
            Buyer.objects.create(username=username, password=password)
            request.session['buyer_username'] = username
            return redirect('catalog')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            buyer = Buyer.objects.get(username=username, password=password)
            request.session['buyer_username'] = buyer.username
            return redirect('catalog')
        except Buyer.DoesNotExist:
            messages.error(request, 'Неверный логин или пароль')

    return render(request, 'login.html')


def user_logout(request):
    if 'buyer_username' in request.session:
        del request.session['buyer_username']
    return redirect('catalog')


def cart(request):
    buyer_username = request.session.get('buyer_username')
    if not buyer_username:
        return redirect('login')

    buyer = get_object_or_404(Buyer, username=buyer_username)
    cart_items = CartItem.objects.filter(buyer=buyer)

    total_price = sum(item.camera.price for item in cart_items)

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


def add_to_cart(request, camera_id):
    buyer_username = request.session.get('buyer_username')
    if not buyer_username:
        return redirect('login')

    buyer = get_object_or_404(Buyer, username=buyer_username)
    camera = get_object_or_404(Camera, id=camera_id)

    CartItem.objects.create(buyer=buyer, camera=camera)
    return redirect('catalog')