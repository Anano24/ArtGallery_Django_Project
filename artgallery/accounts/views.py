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


# Create your views here.



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
    



    