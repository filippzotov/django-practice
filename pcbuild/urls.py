from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path("", pcbuild, name="pcbuild"),
    path("<int:id>", add_piece, name="add-piece"),
]
