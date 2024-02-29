from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutus.html')

def gallery(request):
    return render(request, 'gallery.html')

def contacts(request):
    return render(request, 'contacts.html')