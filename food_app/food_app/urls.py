"""food_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from login import views as login_views
from base_pages import views as base_views
from vendor_pages import views as vendor_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_views.login, name = 'login'),
    path('signup/', login_views.signup, name = 'signup'),
    path('', base_views.home, name = 'home'),
    re_path(r'^account/(?P<username>[\w.@+-]+)/$', base_views.user_home, name = 'account'),
    path('vendors/', base_views.vendor_list, name = 'vendor_list'),
    re_path(r'^vendors/(?P<username>[\w.@+-]+)/$', base_views.user_vendor_list, name = 'user_vendor_list'),
    re_path(r'^myorders/(?P<username>[\w.@+-]+)/$', base_views.user_order, name = 'user_orders'),
    re_path(r'^spec_ven/(?P<vusername>[\w.@+-]+)/(?P<cusername>[\w.@+-]+)/$', base_views.user_vendor_dynamic, name = 'user_specific_vendor'),  
    re_path(r'^profile/(?P<username>[\w.@+-]+)/$', base_views.user_profile, name = 'user_profile'),
    re_path(r'^ven/(?P<username>[\w.@+-]+)/$', vendor_views.list_for_vendors, name = 'vendor_user'),
    path('errora/', login_views.access_error, name = 'error_access'),  
    re_path(r'^checkout/(?P<username>[\w.@+-]+)/$', base_views.user_checkout, name = 'checkout'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include(('payment.urls', 'payment'), namespace = 'payment')),
    re_path(r'^order_status/(?P<username>[\w.@+-]+)/$', vendor_views.order_status, name = "order_status"),
    path('aboutus/', base_views.about_us_v, name = 'about_us'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
