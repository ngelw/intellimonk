from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',HomePage.as_view()),
    path('upload',UploadBook.as_view()),
    path('books',MyBooks.as_view()),
    path('feed',BookFeed.as_view()),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup, name='register'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)