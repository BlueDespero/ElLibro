"""ElLibro URL Configuration

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
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

from LaBiblioteca import views

urlpatterns = [
    path('', RedirectView.as_view(url='biblioteka/')),
    path('biblioteka/', include('LaBiblioteca.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#names
urlpatterns += [
    path('biblioteka/',  views.HomepageView, name='homepage'),
    path('biblioteka/ksiazki', views.BookListView.as_view(), name='ksiazki'),
    path('biblioteka/autorzy', views.AutorListView.as_view(), name='autorzy'),
    path('biblioteka/ksiazki/<int:pk>', views.BookDetailView.as_view(), name='ksiazka-szczegoly'),
    path('biblioteka/autor/<int:pk>', views.AutorDetailView.as_view(), name='autor-szczegoly'),
]