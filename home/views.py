from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def dog(request):
    return render(request,'home/dogpage.html')

def cat(request):
    return render(request,'home/catpage.html')