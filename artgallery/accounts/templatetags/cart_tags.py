from django import template
from orders.models import Cart

register = template.Library()

@register.simple_tag
def cart_item_count(user):
    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=user)
        return sum(item.quantity for item in cart.items.all())
    return 0
