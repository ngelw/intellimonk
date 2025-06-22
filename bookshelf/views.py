from django.shortcuts import render
from django.views import View
from . forms import BookForm
from . models import Book
# Create your views here.
class HomePage(View):
    def get(self,request):
        return render(request,"index.html")
    
class UploadBook(View):
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
    
class MyBooks(View):
    def get(self, request):
        books = Book.objects.filter(addedby=request.user)
        return render(request, "mybooks.html", {"books": books})