from django.urls import path

from . import views


app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name= 'about'),
    path('contact', views.contact_us, name= 'contact'),
    path('blog', views.blog, name= 'blog'),
    path('product_all', views.product_all, name='product_all'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    



    
    
    path('compare', views.compare, name= 'compare'),
    path('login', views.login, name= 'login'),
    path('wishlist', views.wishlist, name= 'wishlist'),
   
    path('my-account', views.my_account, name= 'my-account'),
    path('checkout', views.checkout, name= 'checkout'),
    
    
    
]