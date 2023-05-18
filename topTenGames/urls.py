from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("top40/", views.top40, name="top40"),
    path("decade/", views.decade, name="decade"),
    path("consoles/", views.consoles, name="consoles"),
    path("year/", views.year, name="year"),
    path("sources/", views.sources, name="sources"),
    path("totalsales/", views.totalSales, name="totalsales"),
]