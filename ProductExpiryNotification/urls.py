from django.urls import path
from ProductExpiryNotification import views

app_name = 'ProductExpiryNotification'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='loginPage'),
    path('register/', views.RegisterView.as_view(), name='registerPage'),
    path('logout/', views.LogoutView.as_view(), name='logoutPage'),
    path('home/', views.LoggedInView.as_view(), name='loginHomePage'),
    path('products/', views.ProductCreateView.as_view(), name='addProductPage'),
    path('view_product/', views.ShowProductsView.as_view(), name='viewProductPage')
]
