from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'about.html')


def products(request):
    return render(request,'products.html')

def form(request):
    return render(request,'form.html')
