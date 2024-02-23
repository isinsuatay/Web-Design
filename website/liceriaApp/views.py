from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, CartItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.db.models import Sum
from django.views.decorators.http import require_GET
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required

def HomePage(request):
    return render(request, 'index.html', {'title': "Home Page"})

def category_products(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products_list = Product.objects.filter(category=category)

    paginator = Paginator(products_list, 10)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'product.html', {'category': category, 'products': products})

def contact(request):
    return render(request, 'contact.html')

def help(request):
    return render(request, 'help.html')

def view_cart(request):
    if request.user.is_authenticated:  
        user = request.user
        cart_items = CartItem.objects.filter(user=user)
    else:
        cart = request.session.get('cart', {})
        cart_items = [CartItem(product=Product.objects.get(id=product_id), quantity=item_data['quantity']) for product_id, item_data in cart.items()]

    total_price = sum(item.total_price() for item in cart_items)
    total_items = sum(item.quantity for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price, 'total_items': total_items})

@require_GET
def add_to_cart(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        product_id = request.GET.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        if request.user.is_authenticated:
            user = request.user  
            cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
            return JsonResponse({'message': 'Product added to cart successfully.'})
        else:
            cart = request.session.get('cart', {})
            cart_item = cart.get(str(product_id))

            if cart_item:
                cart_item['quantity'] += 1
            else:
                cart[product_id] = {'quantity': 1}

            request.session['cart'] = cart
            return JsonResponse({'message': 'Product added to cart successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)

def delete_cart_item(request, cart_item_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
        cart_item.delete()
        return JsonResponse({'message': 'Product removed from cart successfully!'})
    else:
        cart = request.session.get('cart', {})
        if cart_item_id in cart:
            del cart[cart_item_id]
            request.session['cart'] = cart
            return JsonResponse({'message': 'Product removed from cart successfully!'})
        else:
            return JsonResponse({'error': 'Cart item not found!'}, status=404)

def clear_cart(request):
    if request.user.is_authenticated:
        CartItem.objects.filter(user=request.user).delete()
    else:
        del request.session['cart']
    return redirect('cart')

def change_cart_item_quantity(request, cart_item_id):
    if request.method == 'GET' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        action = request.GET.get('action')
        cart_item = CartItem.objects.get(id=cart_item_id)

        if action == 'increase':
            cart_item.quantity += 1
            cart_item.save()
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()

        user = request.user
        total_items = CartItem.objects.filter(user=user).aggregate(Sum('quantity'))['quantity__sum'] or 0
        total_price = sum(item.total_price() for item in CartItem.objects.filter(user=user))

        return JsonResponse({'total_items': total_items, 'total_price': total_price})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)


@login_required
def checkout(request):
    if request.method == 'GET':
        cart_items = CartItem.objects.filter(user=request.user)

        try:
            for item in cart_items:
                product = item.product
                if product.stock_quantity >= item.quantity:
                    product.stock_quantity -= item.quantity
                    product.save()
                else:
                    return JsonResponse({'error': 'Insufficient stock.'}, status=400)

                item.delete()

            return JsonResponse({'message': 'Purchase process completed successfully.'})
        except Exception as e:
            return JsonResponse({'error': 'n error occurred during the process.'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)


def order_confirmation(request):
    return render(request, 'order_confirmation.html')
