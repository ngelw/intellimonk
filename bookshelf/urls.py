from django.urls import path
from . views import *
urlpatterns = [
    path('',HomePage.as_view()),
    path('upload',UploadBook.as_view()),
    path('books',MyBooks.as_view()),
]