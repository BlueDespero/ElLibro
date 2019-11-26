from django.urls import path

from . import views

app_name = 'LaBiblioteca'
urlpatterns = [
    path('', views.HomepageView, name='homepage'),
    path('ksiazki/', views.BookListView.as_view(), name='ksiazki'),
]