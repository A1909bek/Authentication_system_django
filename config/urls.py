
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('account/',include('account.urls')),
    path('account/',include('django.contrib.auth.urls')),
]
