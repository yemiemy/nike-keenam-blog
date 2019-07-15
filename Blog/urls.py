"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from post.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/<int:id>', single, name='single'),
    path('search/', search_view, name='search'),
    path('about/', about, name='about'),
    path('blog/<int:id>/like', like_view, name='like'),
    path('blog/<int:id>/like', field_view, name='field'),
    path('contact/', contact, name='contact'),
    path('lifestyle/', lifestyle, name='lifestyle'),
    path('fashion/', fashion, name='fashion'),
    path('food/', food, name='food'),
]

admin.site.site_header = "Nike Keenam Admin"
admin.site.site_title = "Nike Keenam Admin Portal"
admin.site.index_title = "Welcome to Nike Keenam Portal"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)