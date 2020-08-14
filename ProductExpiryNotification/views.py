from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (TemplateView, ListView, CreateView)

from .forms import ProductForm, RegistrationForm, LoginForm
from .models import UserProfile, Product


class IndexView(TemplateView):
    template_name = 'ProductExpiryNotification/index.html'


class RegisterView(CreateView):
    """
    Provides the ability to register a user
    """
    model = UserProfile
    success_url = reverse_lazy('ProductExpiryNotification:loginHomePage')
    form_class = RegistrationForm
    template_name = 'ProductExpiryNotification/Register.html'

    def form_valid(self, form):
        """To login user after successful registration"""
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginUserView(LoginView):
    """
    Provides the ability to login as a user with a username and password
    """
    authentication_form = LoginForm
    template_name = 'ProductExpiryNotification/login.html'

    """
    Set LOGIN_REDIRECT_URL in settings.py to redirect the user after a successful authentication.
    Default = /accounts/profile/
    """
    """
        TODO: Show username in URL pattern for logged in users.
    
    def get_form_kwargs(self):
        # This method is what injects forms with their keyword
        # arguments.
        # grab the current set of form #kwargs
        kwargs = super(LoginUserView, self).get_form_kwargs()
        print(kwargs)
        print(kwargs.keys())
        print(kwargs.values())
        return kwargs
    """


@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'ProductExpiryNotification/AddProducts.html'
    # success_url = reverse_lazy('ProductExpiryNotification:loginHomePage')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = UserProfile.objects.get(user=self.request.user)
            user.bought.add(form.save(commit=True))
            return redirect('ProductExpiryNotification:loginHomePage')

        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class ShowProductsView(ListView):
    model = Product
    template_name = "ProductExpiryNotification/ViewProducts.html"
    context_object_name = 'product_list'

    def get_context_data(self, **kwargs):
        context = super(ShowProductsView, self).get_context_data(**kwargs)
        products = self.get_queryset()
        context['products'] = products
        return context

    def get_queryset(self):
        user = UserProfile.objects.get(user=self.request.user)
        product_set = list(Product.objects.filter(bought_by=user))
        product_ids = [product_item.id for product_item in product_set]
        return Product.objects.filter(id__in=product_ids)


@method_decorator(login_required, name='dispatch')
class LoggedInView(TemplateView):
    template_name = 'ProductExpiryNotification/LoginHomePage.html'
    model = UserProfile
    slug_field = "user"
    # slug_url_kwarg = "user"

    def get_object(self):
        user_object = get_object_or_404(UserProfile, user=self.kwargs.get("user"))

        # only owner can view his page
        if self.request.user.username == user_object.user.username:
            return user_object.user.username
        else:
            # redirect to 404 page
            print("you are not the owner!!")


@method_decorator(login_required, name='dispatch')
class LogoutView(TemplateView):
    template_name = 'ProductExpiryNotification/index.html'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request)
