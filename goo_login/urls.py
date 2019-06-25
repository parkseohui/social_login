from django.contrib import admin
from django.urls import path,include
from . import views
import goo_login.views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',views.home,name='home'),
    path('accounts/', include('allauth.urls')),

]
