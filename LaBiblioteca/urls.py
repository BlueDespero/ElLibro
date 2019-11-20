from django.urls import path

from . import views

app_name = 'LaBiblioteca'
urlpatterns = [
    path('', views.HomepageView, name='Strona główna'),
]