from django.shortcuts import render
from django.views import View
from . forms import BookForm
from . models import Book, UserImage
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
import random
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "index.html", {"success": "Login successful!"})
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "authentication/login.html")
def logout_view(request):
    logout(request)
    return render(request, "authentication/login.html", {"success": "Logout successful!"})
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if not username or not password or not email:
            return render(request, "authentication/signup.html", {"error": "All fields are required"})
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return render(request, "authentication/login.html", {"success": "Signup successful! Please login."})
        except Exception as e:
            return render(request, "authentication/signup.html", {"error": str(e)})
    return render(request, "authentication/signup.html")
class HomePage(View):
    def get(self,request):
        return render(request,"index.html")
    
class UploadBook(LoginRequiredMixin, View):
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.addedby = request.user  
            book.save()
            context = {"form": BookForm(), "success": "Book uploaded successfully!"}
            return render(request, "upload.html", context)
        else:
            context = {"form": form}
            return render(request, "upload.html", context)

    def get(self, request):
        return render(request, "upload.html", {"form": BookForm()})


class MyBooks(LoginRequiredMixin, View):
    def get(self, request):
        books = Book.objects.filter(addedby=request.user)
        author_image = UserImage.objects.filter(user=request.user).first()
        return render(request, "mybooks.html", {"books": books, "author_image": author_image})

class BookFeed(View):
    def get(self, request):
        books = list(Book.objects.filter(privacy='public').select_related('addedby'))
        random.shuffle(books)
        # Attach profile images for each book's author
        author_images = {}
        for book in books:
            user = book.addedby
            image_obj = UserImage.objects.filter(user=user).first()
            book.author_image = image_obj.image if image_obj and image_obj.image else None
        return render(request, "displaypage.html", {"books": books})