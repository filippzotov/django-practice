from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("consoles/", consoles, name="consoles"),
    path("makenews/", make_news, name="makenews"),
    path("consoles/<int:company_id>/", company_consoles, name="consoles1"),
    re_path(
        r"console/(?P<pk>\d+)$", ConsoleDetailView.as_view(), name="console-detail"
    ),
    ##re_path(r"news/(?P<pk>\d+)$", NewsDetailView.as_view(), name="news-detail"),
    re_path(r"news/(?P<pk>\d+)$", detail_comment, name="news-detail"),
]
