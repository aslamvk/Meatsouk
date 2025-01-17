"""
URL configuration for meatsouk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_meatsouk.urls')),
    path('adminn/', include('admin_side.urls')),
    path('products/', include('products.urls')),
    path('category/', include('category.urls')),
    path('user_page/', include('admin_user.urls')),
    path('account/', include('allauth.urls')),
    path('user_profile/', include('user.urls')),
    path('address/', include('address.urls')),
    path('admin_pincode/', include('pincode.urls')),
    path('', include('cart.urls')),
    path('checkout/', include('order.urls')),
    path('wallet/', include('wallet.urls')),
    path('coupon/', include('coupon.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('offer/', include('offer.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)