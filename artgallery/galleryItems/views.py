from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, CreateView
from .models import GalleryItems
from .forms import GalleryItemsForm
from django.forms import BaseModelForm

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        

        items = GalleryItems.objects.all()


        return render(request, self.template_name, {'items': items})
    



class AddItemView(CreateView):
    model = GalleryItems
    form_class = GalleryItemsForm
    template_name = "add_gallery_item.html"
    success_url = "/"
    # permission_required = "mainapp.add_event"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.save()

        return super().form_valid(form)
    
    
    


    

    



