from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GalleryItems, Cart, CartItem
from django.contrib import messages



@login_required
def add_to_cart(request, item_id):
    product = get_object_or_404(GalleryItems, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Check if the item is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        # If the item is already in the cart, update the quantity
        cart_item.quantity += 1
        cart_item.save()
    else:
        # If the item is not in the cart, add it with quantity 1
        cart_item.quantity = 1
        cart_item.save()
    
    return redirect('galleryItems:shop')


@login_required
def delete_from_cart(request, item_id):
    product = get_object_or_404(GalleryItems, id=item_id)
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    
    if cart_item:
        cart_item.delete()
        messages.success(request, 'Item removed from your cart.')
    else:
        messages.info(request, 'Item was not found in your cart.')

    return redirect('accounts:profile')
