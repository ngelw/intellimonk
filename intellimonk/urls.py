from django.contrib import admin
from django.urls import path,include
import bookshelf.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(bookshelf.urls)),
]
