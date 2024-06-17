from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView
from django.http.response import (
    HttpResponse as HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)
from .forms import RegistrationForm
from django.contrib.auth import logout, login, update_session_auth_hash
from django.forms import BaseModelForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from orders.models import Cart
from typing import Any




class UserSignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('galleryItems:homepage')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response



class UserLoginView(LoginView, UserPassesTestMixin):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('galleryItems:homepage')

    def test_func(self) -> bool | None:
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self) -> HttpResponseRedirect:
        return redirect('galleryItems:homepage')
    



@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        context['cart'] = cart
        context['items'] = cart.items.all()
        context['item_count'] = sum(item.quantity for item in cart.items.all())
        return context

    

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "password_change_form.html"
    success_url = "/password_change_done/"


    def form_valid(self, form: Any) -> HttpResponse:
        user = form.save()
        update_session_auth_hash(self.request, user)
        return super().form_valid(form)   




    