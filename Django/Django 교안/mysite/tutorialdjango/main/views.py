from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')

def product(request):
    return render(request,'main/product.html')

def productdetails(request, pk):
    data = {
        'value': pk + 100,
        'one': [1, 2, 3, 4],
        'two': {'hello': 100, 'world': 200}
    }
    return render(request, 'main/productdetails.html', data)
def a(request):
    return render(request,'main/a.html')

def b(request):
    return render(request,'main/b.html')

def c(request):
    return render(request,'main/c.html')
