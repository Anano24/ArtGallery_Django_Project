from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, CreateView, DeleteView, UpdateView
from .models import GalleryItems
from .forms import GalleryItemsForm
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.http.response import HttpResponse as HttpResponse, HttpResponseRedirect
from orders.models import Cart, CartItem
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.



class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        items = GalleryItems.objects.all()
        
        return render(request, self.template_name, {'items': items})
    

        

class ShopView(TemplateView):
    template_name = 'shop.html'
    
    def get(self, request, *args, **kwargs):
        cart_items = []
        query = request.GET.get("query")

        if query:
            items = GalleryItems.objects.filter(
                Q(title__icontains=query)
            )
            print(f"Filtered items: {items}")
        else:
            items = GalleryItems.objects.all().order_by('id')


        paginator = Paginator(items, 6)
        page_number = request.GET.get('page')
        items = paginator.get_page(page_number)


        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart).values_list('product_id', flat=True)

        return render(request, self.template_name, {'items': items, 'cart_items': cart_items})
    



class AddItemView(PermissionRequiredMixin, CreateView):
    model = GalleryItems
    form_class = GalleryItemsForm
    template_name = "add_gallery_item.html"
    success_url = reverse_lazy('galleryItems:shop')
    permission_required = "galleryItems.add_item"


    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()

        return super().form_valid(form)
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect('galleryItems:shop')



class EditItemView(PermissionRequiredMixin, UpdateView):
    model = GalleryItems
    form_class = GalleryItemsForm
    template_name = "edit_gallery_item.html"
    success_url = reverse_lazy('galleryItems:shop')
    permission_required = "galleryItems.edit_item"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect('galleryItems:shop')

 
    
class DeleteItemView(PermissionRequiredMixin, DeleteView):
    model = GalleryItems
    template_name = 'delete.html'
    success_url = reverse_lazy('galleryItems:shop')
    permission_required = 'galleryItems.delete_item'


    def test_func(self) -> bool | None:
        return self.request.user.is_superuser

    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect('galleryItems:homepage')
    


class ItemDetailView(DetailView):
    template_name = 'detailed_item.html'

    def get(self, request, *args, **kwargs):
        item_id = kwargs.get('pk')
        detailed_item = get_object_or_404(GalleryItems, pk=item_id)
        in_cart = False

        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user)
            in_cart = CartItem.objects.filter(cart=cart, product=detailed_item).exists()

        context = {
            'detailed_item': detailed_item,
            'in_cart': in_cart
        }
        return render(request, self.template_name, context)
    



